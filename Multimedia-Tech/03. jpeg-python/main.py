import numpy as np
from skimage.io import imread, imsave, imshow
from scipy.fftpack import dct, idct

# Algorithm
# 1. rgb2yuv
# 2. decimate (укрупнение пикселей)
# 3. разбиваем на блоки 8х8
# 4. dct для каждого блока
# 5. делим нацело на матрицы квантования
# 6. превращаем блок в зигзаг
# 7. кодируем используя метод хаффмана и rle
# 8. записываем в файл все параметры (мета-данные)
# 9. прочитываем файл с мета-данными
# 10. декодируем код хаффмана
# 11. превращаем зигзаг в блок
# 12. умножаем на матрицы квантования
# 13. idct для каждого блока
# 14. собираем из блоков 8x8 yuv-картинку (interpolate)
# 15. yuv2rgb


def lum_or_color(matrix):
    if matrix == "lum":
        return np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                    [12, 12, 14, 19, 26, 58, 60, 55],
                    [14, 13, 16, 24, 40, 57, 69, 56],
                    [14, 17, 22, 29, 51, 87, 80, 62],
                    [18, 22, 37, 56, 68, 109, 103, 77],
                    [24, 35, 55, 64, 81, 104, 113, 92],
                    [49, 64, 78, 87, 103, 121, 120, 101],
                    [72, 92, 95, 98, 112, 100, 103, 99]])

    elif matrix == "color":
        return np.array([[17, 18, 24, 47, 99, 99, 99, 99],
                [18, 21, 26, 66, 99, 99, 99, 99],
                [24, 26, 56, 99, 99, 99, 99, 99],
                [47, 66, 99, 99, 99, 99, 99, 99],
                [99, 99, 99, 99, 99, 99, 99, 99],
                [99, 99, 99, 99, 99, 99, 99, 99],
                [99, 99, 99, 99, 99, 99, 99, 99],
                [99, 99, 99, 99, 99, 99, 99, 99]])


def rgb2yuv(img):
    x_form = np.array([[.299, .587, .114], [-.1687, -.3313, .5], [.5, -.4187, -.0813]])
    new_img = img.dot(x_form.T)
    new_img[:, :, [1, 2]] += 128

    return new_img.astype(np.uint8)


def yuv2rgb(img):
    x_form = np.array([[1, 0, 1.402], [1, -0.34414, -0.71414], [1, 1.772, 0]])
    rgb = img
    rgb[:, :, [1, 2]] -= 128
    rgb = rgb.dot(x_form.T)

    return np.clip(rgb, 0, 255).astype(np.uint8)


def decimate(img, block_size):
    rows, cols = img.shape[0], img.shape[1]
    blocks_count = rows // block_size * cols // block_size if (rows // block_size) and (cols // block_size) else None
    top_left_cells = np.empty((blocks_count, 3), dtype=np.int32)
    oth_cells = np.empty((blocks_count, 63, 3), dtype=np.int32)
    return rows, cols, blocks_count, top_left_cells, oth_cells


def interpolate(block_size, blocks_count):
    image_size = int(np.sqrt(blocks_count)) * block_size
    blocks_per_line = image_size // block_size
    img = np.empty((image_size, image_size, 3), dtype=np.uint8)
    return img, blocks_per_line


def center_on_zero(img, i, j, k, block_size):
    return img[i: i + block_size, j: j + block_size, k] - 128


def return_center(img, i, j, k, block_size, block):
    img[i: i + block_size, j: j + block_size, k] = block + 128
    return img


def do_dct(img):
    return dct(dct(img.T, norm='ortho').T, norm='ortho')


def undo_dct(img):
    return idct(idct(img.T, norm='ortho').T, norm='ortho')


def quantize(block, matrix):
    quant_matrix = lum_or_color(matrix)
    return block // quant_matrix


def dequantize(block, matrix):
    quant_matrix = lum_or_color(matrix)
    return block * quant_matrix


def zigzag_points(rows, cols):
    # constants for directions
    UP, DOWN, RIGHT, LEFT, UP_RIGHT, DOWN_LEFT = range(6)

    # move the point in different directions
    def move(direction, point):
        return {
            UP: lambda point: (point[0] - 1, point[1]),
            DOWN: lambda point: (point[0] + 1, point[1]),
            LEFT: lambda point: (point[0], point[1] - 1),
            RIGHT: lambda point: (point[0], point[1] + 1),
            UP_RIGHT: lambda point: move(UP, move(RIGHT, point)),
            DOWN_LEFT: lambda point: move(DOWN, move(LEFT, point))
        }[direction](point)

    # return true if point is inside the block bounds
    def inbounds(point):
        return 0 <= point[0] < rows and 0 <= point[1] < cols

    # start in the top-left cell
    point = (0, 0)

    # True when moving up-right, False when moving down-left
    move_up = True

    for i in range(rows * cols):
        yield point
        if move_up:
            if inbounds(move(UP_RIGHT, point)):
                point = move(UP_RIGHT, point)
            else:
                move_up = False
                if inbounds(move(RIGHT, point)):
                    point = move(RIGHT, point)
                else:
                    point = move(DOWN, point)
        else:
            if inbounds(move(DOWN_LEFT, point)):
                point = move(DOWN_LEFT, point)
            else:
                move_up = True
                if inbounds(move(DOWN, point)):
                    point = move(DOWN, point)
                else:
                    point = move(RIGHT, point)


def block_to_zigzag(block):
    return np.array([block[point] for point in zigzag_points(*block.shape)])


def zigzag_to_block(zigzag):
    rows = cols = int(np.sqrt(len(zigzag)))

    block = np.empty((rows, cols), np.int32)

    for i, point in enumerate(zigzag_points(rows, cols)):
        block[point] = zigzag[i]

    return block


def huffman_rle(img):
    pass


def encode(img, block_size):

    yuv_img = rgb2yuv(img)
    rows, cols, blocks_count, top_left_cells, oth_cells = decimate(yuv_img, block_size)
    block_index = 0

    for i in range(0, rows, block_size):
        for j in range(0, cols, block_size):
            block_index += 1

            for k in range(3):
                block = center_on_zero(yuv_img, i, j, k, block_size)
                dct_matrix = do_dct(block)
                quant_matrix = quantize(dct_matrix, "lum" if k == 0 else "color")
                zigzag_block = block_to_zigzag(quant_matrix)

                top_left_cells[block_index if block_index < blocks_count else blocks_count - 1, k] = zigzag_block[0]
                oth_cells[block_index if block_index < blocks_count else blocks_count - 1, :, k] = zigzag_block[1:]

    return top_left_cells, oth_cells, blocks_count


def decode(img, block_size):

    top_left_cells, oth_cells, blocks_count = img
    new_img, blocks_per_line = interpolate(block_size, blocks_count)

    for block_index in range(blocks_count):
        i = block_index // blocks_per_line * block_size
        j = block_index % blocks_per_line * block_size

        for k in range(3):
            zigzag = [top_left_cells[block_index, k]] + list(oth_cells[block_index, :, k])
            quant_matrix = zigzag_to_block(zigzag)
            dct_matrix = dequantize(quant_matrix, "lum" if k == 0 else "color")
            block = undo_dct(dct_matrix)

            new_img = return_center(new_img, i, j, k, block_size, block)

    rgb_img = yuv2rgb(new_img.astype(np.uint8))

    return rgb_img


def main():
    img = imread('image.jpg')
    block_size = 8
    enc_img = encode(img, block_size)
    dec_img = decode(enc_img, block_size)
    imsave('decoded_img.jpg', dec_img)


if __name__ == "__main__":
    main()
