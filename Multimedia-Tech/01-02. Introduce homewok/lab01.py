from skimage.io import imread, imsave, imshow
import numpy as np


def low_bright_quant(img, level):
    return np.round(img / level)


def low_bright_reset(img, level):
    low_img = low_bright_quant(img, level) * level
    low_img = np.clip(low_img, 0, 255 - level).astype('uint8')
    imsave('low_bright_image_' + str(level) + '_.jpg', low_img)
    imshow(low_img)

    return low_img


# _1.2 RGB2YUV. Децимация цветоразностных каналов._


def rgb2yuv(img):
    x_form = np.array([[.299, .587, .114], [-.1687, -.3313, .5], [.5, -.4187, -.0813]])
    y_cbcr = img.dot(x_form.T)
    y_cbcr[:, :, [1, 2]] += 128

    return y_cbcr.astype('uint8')


def yuv2rgb(img):
    x_form = np.array([[1, 0, 1.402], [1, -0.34414, -0.71414], [1, 1.772, 0]])
    rgb = img.astype(np.float)
    rgb[:, :, [1, 2]] -= 128
    rgb = rgb.dot(x_form.T)
    np.putmask(rgb, rgb > 255, 255)
    np.putmask(rgb, rgb < 0, 0)

    return rgb.astype('uint8')


def decimation_1st(img, block_size):
    y, u, v = img[:, :, 0], img[:, :, 1], img[:, :, 2]

    new_u = np.array([np.array([px for j, px in enumerate(row) if j % block_size]) for i, row in enumerate(u) if i % block_size])
    new_v = np.array([np.array([px for j, px in enumerate(row) if j % block_size]) for i, row in enumerate(v) if i % block_size])

    return y.astype('uint8'), new_u.astype('uint8'), new_v.astype('uint8')


def decimation_2nd(u, v, img, block_size):
    y = img[:, :, 0]

    new_u = np.array(np.repeat([np.repeat([px for px in row], block_size) for row in u], block_size, axis=0))
    new_v = np.array(np.repeat([np.repeat([px for px in row], block_size) for row in v], block_size, axis=0))

    new_img = np.dstack((y, new_u, new_v))

    return new_img.astype('uint8'), new_u.astype('uint8'), new_v.astype('uint8')


# _1.3 Энтромия и MSE_


def entropy(img):
    freq = np.array([0 for i in range(256)])

    for row in img:
        for px in row:
            freq[px] += 1

    n = len(img) * len(img[0])
    freq = freq / n
    ent = -np.sum([p * np.log2(p) for p in freq if p != 0])

    return ent


def mse(img_0, img_1):
    return np.sqrt(
        np.sum([(px_0 - px_1) ** 2 for px_0, px_1 in zip(img_0[:, :], img_1[:, :])]) / len(img_1) / len(img_1[0]))


if __name__ == "__main__":
    img = imread('image.jpg')
    decoded = imread('decoded.jpg')
    print(entropy(img))
    print(entropy(decoded))
    # img = imread('image.jpg')
    # img = img.astype('uint8')
    # imshow(img)
    # print("Entropy of the original image:", entropy(img))
    #
    # # rgb2greyscale
    # grey_img, _, _ = decimation_1st(rgb2yuv(img), 2)
    # imshow(grey_img)
    # imsave('grey_image.jpg', grey_img)
    # print("Entropy of the greyscale image:", entropy(grey_img))
    #
    # low_fi = low_bright_quant(grey_img, 4)
    # low_fi = low_bright_reset(grey_img, 4)
    # print("Entropy of low bright:", entropy(low_fi))
    #
    # low_fi = low_bright_quant(grey_img, 8)
    # low_fi = low_bright_reset(grey_img, 8)
    # print("Entropy of low bright:", entropy(low_fi))
    #
    # low_fi = low_bright_quant(grey_img, 16)
    # low_fi = low_bright_reset(grey_img, 16)
    # print("Entropy of low bright:", entropy(low_fi))
    #
    # low_fi = low_bright_quant(grey_img, 32)
    # low_fi = low_bright_reset(grey_img, 32)
    # print("Entropy of low bright:", entropy(low_fi))
    #
    # low_fi = low_bright_quant(grey_img, 64)
    # low_fi = low_bright_reset(grey_img, 64)
    # print("Entropy of low bright:", entropy(low_fi))
    #
    # print("MSE of the greyscale from the low bright:", mse(grey_img, low_fi))
    #
    # yuv_img = rgb2yuv(img)
    # imsave('yuv_image.jpg', yuv_img)
    # imshow(yuv_img)
    #
    # print('Entropy of original image:', entropy(img))
    # print('Entropy of yuv image:', entropy(yuv_img))
    #
    # _, dec_u_img, dec_v_img = decimation_1st(yuv_img, 2)
    # dec_yuv_img, _, _ = decimation_2nd(dec_u_img, dec_v_img, yuv_img, 2)
    # imshow(dec_yuv_img)
    # imsave('dec_yuv_image.jpg', dec_yuv_img)
    #
    # print('Entropy of yuv-image after decimation:', entropy(dec_yuv_img))
    #
    # rgb_img = yuv2rgb(dec_yuv_img)
    # imshow(rgb_img)
    # imsave('decoded_image.jpg', rgb_img)
    #
    # print('Entropy of yuv image:', entropy(dec_yuv_img))
    # print('Entropy of rgb image:', entropy(rgb_img))
    #
    # print('MSE of the original image from the decoded:', mse(img, rgb_img))
    #
    # imshow(dec_u_img)
    # imsave('dec_u_image.jpg', dec_u_img)
    #
    # print('Entropy of u-channel:', entropy(dec_u_img))
    #
    # imshow(dec_v_img)
    # imsave('dec_v_image.jpg', dec_v_img)
    #
    # print('Entropy of v-channel:', entropy(dec_v_img))
    #
    # # entropy of rgb for each channel vs. entropy of rgb img
    # r, g, b = img[:, :, 0], img[:, :, 1], img[:, :, 2]
    # print("Entropy of RGB-image:", entropy(img))
    # print("Entropy for each channel:", entropy(r), entropy(g), entropy(b))
    #
    # # entropy of decoded_rgb for each channel vs. entropy of decoded_rgb_img
    # r, g, b = rgb_img[:, :, 0], rgb_img[:, :, 1], rgb_img[:, :, 2]
    # print("Entropy of RGB-image after decimation:", entropy(rgb_img))
    # print("Entropy for each channel:", entropy(r), entropy(g), entropy(b))
