import numpy as np
from skimage.io import imread


def entropy(img):
    freq = np.array([0 for i in range(256)])

    for row in img:
        for px in row:
            freq[px] += 1

    n = len(img) * len(img[0])
    freq = freq / n
    ent = -np.sum([p * np.log2(p) for p in freq if p != 0])

    return ent


def rmse(img1, img2):
    return np.sqrt(np.sum(np.power(img1 - img2, 2)) / img1.shape[0] / img1.shape[1])


def psnr(img1, img2):
    rmse_val = rmse(img1, img2)

    if rmse_val == 0: return 100

    px__max = 255.0

    return 20 * np.log10(px__max / np.sqrt(rmse_val))


if __name__ == "__main__":

    img = imread('image.jpg')
    decoded = imread('decoded.jpg')
    print(entropy(img))
    print(entropy(decoded))
    print(psnr(img, decoded))
