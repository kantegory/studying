from random import *
from time import *


def correct_order(data):
    count = 0
    while count + 1 < len(data):
        if data[count] > data[count + 1]:
            return False
        count += 1
    return True


def bogosort(data):
    while not correct_order(data):
        shuffle(data)   # randomize data
    return data


if __name__ == "__main__":

    data = [randint(0, 100) for i in range(10)]
    start = time()
    print("Before: ", data)
    data = bogosort(data)
    print("After: ", data)
    print("%.2f seconds" % (time() - start))
