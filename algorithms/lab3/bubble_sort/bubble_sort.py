from random import randint


def bubble_sort(data):
    for i in range(len(data)):
        for j in range(len(data) - 1, i, -1):
            if data[j] < data[j - 1]:
                data[j], data[j - 1] = data[j - 1], data[j]

    return data


if __name__ == "__main__":
    data = [randint(0, 100) for i in range(10)]
    print('Before:', data)
    print('After:', bubble_sort(data))
