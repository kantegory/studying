from random import randint


def heapify(data, nums, root):
    largest = root
    left = 2 * root + 1
    right = 2 * root + 2

    if left < nums and data[root] < data[left]:
        largest = left

    if right < nums and data[largest] < data[right]:
        largest = right

    if largest != root:
        data[root], data[largest] = data[largest], data[root]
        heapify(data, nums, largest)


def heapsort(data):
    for root in range(len(data), -1, -1):
        heapify(data, len(data), root)

    for root in range(len(data) - 1, 0, -1):
        data[root], data[0] = data[0], data[root]  # swap
        heapify(data, root, 0)


if __name__ == "__main__":
    data = [randint(0, 100) for i in range(10)]
    print("Unsorted array is", data)
    heapsort(data)
    print("Sorted array is")
    for i in range(len(data)):
        print("%d" % data[i])
