from random import randint
from time import *


def merge_sort(data):

    if len(data) > 1:
        middle = len(data) // 2
        left_half = data[:middle]
        right_half = data[middle:]

        print('break:', left_half, right_half)

        # recursion
        merge_sort(left_half)
        merge_sort(right_half)

        # vars for whiles
        i = 0
        j = 0
        k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                data[k]=left_half[i]
                i += 1
            else:
                data[k]=right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            data[k]=left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            data[k]=right_half[j]
            j += 1
            k += 1

        print('merge:', data)


if __name__ == "__main__":
    start = time()
    data = [randint(0, 100) for i in range(10)]
    merge_sort(data)
    print("%.2f seconds" % (time() - start))
