from random import randint, choice
from time import *


def quick_sort(data):
    if len(data) <= 1:
        return data
    else:
        rand_elem = choice(data)

    right_data = [elem for elem in data if elem < rand_elem]
    middle_data = [rand_elem] * data.count(rand_elem)
    left_data = [elem for elem in data if elem > rand_elem]

    return quick_sort(right_data) + middle_data + quick_sort(left_data)


if __name__ == "__main__":

    data = [randint(0, 100) for i in range(10)]
    start = time()
    print('!Sorted:', data)
    print('Sorted:', quick_sort(data))
    print("%.2f seconds" % (time() - start))
