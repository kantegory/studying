import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imsave
from skimage.exposure import histogram
from skimage.util import random_noise
from skimage import img_as_float
from scipy.ndimage.filters import median_filter
from PIL import Image, ImageFilter, ImageChops
import cv2 as cv


def rgb2gray(img):
    x_form = np.array([[.299, .587, .114], [-.1687, -.3313, .5], [.5, -.4187, -.0813]])
    y_cbcr = img.dot(x_form.T)
    y_cbcr[:, :, [1, 2]] += 128

    return y_cbcr.astype('uint8')[:, :, 0]


# 2.1 Гистограмма яркостей
def create_hist(img):
    # hist, bins = np.histogram(img.flatten(), 256, [0, 256])

    plt.hist(img.flatten(), 256, [0, 256], color='black')
    plt.xlim([0, 256])
    plt.show()


# Робастное линейное рястяжение
def brle(img, pct):
    y, x = histogram(img)
    xmin, xmax = int(np.percentile(x, pct)), int(np.percentile(x, 100 - pct))
    new_img = np.array([np.array([
        np.clip(np.uint8((px - xmin) * (255 / (xmax - xmin))), 0, 255)
        for px in row]) for row in img])
    return new_img


# карта разности, для неё нужен импорт: from skimage import img_as_float
def diff_map(img1, img2, name="img1_img2"):
    _diff_map = np.abs(img_as_float(img1) - img_as_float(img2))
    imsave('diff_map_' + str(name) + '.jpg', _diff_map)
    return _diff_map


def docked_map(img1, img2, name="img1_img2"):
    new_img = img1.copy()
    for px in range(len(new_img) // 2, len(new_img)):
        new_img[px] = img2[px]
    imsave('docked_map_' + str(name) + '.jpg', new_img.astype('uint8'))
    return new_img.astype('uint8')


# 2.2 Растяжение по каналам


def exp(img):
    y, x = histogram(img)
    xmin, xmax = int(np.percentile(x, 0)), int(np.percentile(x, 100))
    new_img = np.array([np.array([np.uint8((px - xmin) * (255 / (xmax - xmin))) for px in row]) for row in img])
    return new_img


def foreach_channel(img):
    r = exp(img[:, :, 0])
    g = exp(img[:, :, 1])
    b = exp(img[:, :, 2])
    return np.dstack((r, g, b))


def gray_world(img):
    av = np.mean(img)
    r, g, b = np.clip((av / np.mean(img[:, :, 0])) * img[:, :, 0], 0, 255), np.clip(
        (av / np.mean(img[:, :, 1])) * img[:, :, 1], 0, 255), np.clip((av / np.mean(img[:, :, 2])) * img[:, :, 2], 0,
                                                                      255)
    new_img = np.dstack((r, g, b)).astype('uint8')
    return new_img


# 2.4
def convolution(img, kernel):
    kernel_shape = kernel.shape[0]
    kernel = np.flipud(np.fliplr(kernel))

    output = np.zeros_like(img)

    img_padded = np.zeros((img.shape[0] + kernel_shape, img.shape[1] + kernel_shape))

    img_padded[1: - kernel_shape + 1, 1: - kernel_shape + 1] = img
    for x in range(img.shape[1]):
        for y in range(img.shape[0]):
            output[y, x] = (kernel * img_padded[y: y + kernel_shape, x: x + kernel_shape]).sum()

    return output


if __name__ == "__main__":
    img = imread('img.jpg')

    gray_img = rgb2gray(img)

    imsave("gray_img.jpg", gray_img)

    gaussian_3_9x9 = cv.GaussianBlur(gray_img, (9, 9), 10.0, 3)
    cv.imwrite('gaussian_3_9x9.jpg', gaussian_3_9x9)
    gaussian_6_9x9 = cv.GaussianBlur(gray_img, (9, 9), 10.0, 6)
    cv.imwrite('gaussian_6_9x9.jpg', gaussian_6_9x9)
    gaussian_3_15x15 = cv.GaussianBlur(gray_img, (15, 15), 10.0, 3)
    cv.imwrite('gaussian_3_15x15.jpg', gaussian_3_15x15)


    # print(img.shape)
    #
    # create_hist(img)
    #
    # brle_img = brle(img, 5)
    # imsave('brle_img.jpg', brle_img)
    #
    # # Гистограмма яркостей после растяжения
    #
    # create_hist(brle_img)
    #
    # diff_map_brle = diff_map(img, brle_img, name="img_brle-img")
    #
    # docked_map_brle = docked_map(img, brle_img, name="img_brle-img")
    # exp_img = foreach_channel(img)
    # imsave('exp_img.jpg', exp_img)
    #
    # docked_map_exp = docked_map(img, exp_img, "img_exp-img")
    #
    # # Гистограмма яркостей после растяжения
    # create_hist(exp_img)
    #
    # diff_map_exp = diff_map(img, exp_img, name="img_exp-img")
    #
    # img = imread('image1.jpg')
    #
    # gray_img = rgb2gray(img)
    # imsave('gray_img.jpg', gray_img)
    #
    # gw_img = gray_world(img)
    # imsave('gw_img.jpg', gw_img)
    #
    # docked_map_gw = docked_map(img, gw_img, "img_gw-img")
    #
    # # 2.3
    #
    # sp_gray_img = random_noise(gray_img, mode="s&p", seed=None, clip=True)
    #
    # docked_map_sp = docked_map(gray_img, sp_gray_img, "gray-img_sp-gray-img")
    #
    # diff_map_sp = diff_map(img_as_float(gray_img), img_as_float(sp_gray_img), "gray-img_sp-gray-img")
    #
    # filtered_img = median_filter(sp_gray_img, 3)
    #
    # diff_map_filtered = diff_map(img_as_float(gray_img), img_as_float(filtered_img), "gray-img_filtered-img")
    #
    # # Усреднение
    # # kernel = np.array([[1 / 9, 1 / 9, 1 / 9],[1 / 9, 1 / 9, 1 / 9],[1 / 9, 1 / 9, 1 / 9]])
    # kernel = np.array([[1 / 25, 1 / 25, 1 / 25, 1 / 25, 1 / 25], [1 / 25, 1 / 25, 1 / 25, 1 / 25, 1 / 25], [1 / 25, 1 / 25, 1 / 25, 1 / 25, 1 / 25], [1 / 25, 1 / 25, 1 / 25, 1 / 25, 1 / 25], [1 / 25, 1 / 25, 1 / 25, 1 / 25, 1 / 25]])
    # av_img = convolution(gray_img, kernel)
    # imsave('av_img.jpg', av_img)
    # # Автоусреднение
    # pilgray = Image.open('gray_img.jpg')
    # autoav_img = pilgray.filter(ImageFilter.SMOOTH)
    # autoav_img.save('autoav.jpg')
    # autoav_img = imread('autoav.jpg')
    #
    # docked_map_av = docked_map(av_img, autoav_img, "av-img_autoav-img")
    #
    # diff_map_av = diff_map(img_as_float(av_img), img_as_float(autoav_img), "av-img_autoav-img")
    #
    # # Сдвиг на 1
    # kernel = np.array([[0, 0, 0], [1, 0, 0], [0, 0, 0]])
    # shift_1 = convolution(gray_img, kernel)
    #
    # # Автосдвиг
    # pilgray = Image.open('gray_img.jpg')
    # autoshift = ImageChops.offset(pilgray, 1, 0)
    # autoshift.save('autoshift.jpg')
    # autoshift = imread('autoshift.jpg')
    #
    # docked_map_shift = docked_map(shift_1, autoshift, "shift_autoshift")
    #
    # diff_map_shift = diff_map(img_as_float(shift_1), img_as_float(autoshift), "shift_autoshift")
    #
    # Гауссов фильтр
    kernel = np.array([[0.07511361, 0.1238414, 0.07511361], [0.1238414, 0.20417996, 0.1238414], [0.07511361, 0.1238414, 0.07511361]])
    gauss = convolution(gray_img, kernel)
    imsave("gauss.jpg", gauss)
    #
    # # Автогаусс
    # pilgray = Image.open('gray_img.jpg')
    # autogauss = pilgray.filter(ImageFilter.GaussianBlur)
    # autogauss.save('autogauss.jpg')
    # autogauss = imread('autogauss.jpg')
    #
    # docked_map_gauss = docked_map(gauss, autogauss, "gauss_autogauss")
    #
    # diff_map_gauss = diff_map(img_as_float(gauss), img_as_float(autogauss), "gauss_autogauss")
    #
    # # Повышение резкости
    # kernel = np.array([[0, -0.04, 0], [-0.04, 2, -0.04], [0, -0.04, 0]])
    # sharp = convolution(gray_img, kernel)
    #
    # # Авторезкость
    # pilgray = Image.open('gray_img.jpg')
    # autosharp = pilgray.filter(ImageFilter.SHARPEN)
    # autosharp.save('autosharp.jpg')
    # autosharp = imread('autosharp.jpg')
    #
    # docked_map_sharp = docked_map(sharp, autosharp, "sharp_autosharp")
    #
    # diff_map_sharp = diff_map(img_as_float(sharp), img_as_float(autosharp), "sharp_autosharp")
    #
    # # 2.5 Unsharp mask
    # gaussian_3 = cv.GaussianBlur(gray_img, (9, 9), 10.0)
    # unsharp_img = cv.addWeighted(gray_img, 1.5, gaussian_3, -0.5, 0, gray_img)
    # cv.imwrite('unsharp_img.jpg', unsharp_img)
    #
    # unsharp_img = imread('unsharp_img.jpg')
    #
    # docked_map_unsharp = docked_map(unsharp_img, autosharp, "unsharp_autosharp")
    #
    # diff_map_unsharp = diff_map(img_as_float(unsharp_img), img_as_float(autosharp), "unsharp_autosharp")
