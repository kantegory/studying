def binary_search(data, elem):
    """
    :param data: sorted array of ints
    :param elem: founded elem
    :return: boolean (answer on question: "Is elem on array or not?"
    """
    left = 0
    right = len(data) - 1
    found = False

    while left <= right and not found:
        
        middle = (left + right) // 2

        if data[middle] == elem:
            found = True
        else:
            if elem < data[middle]:
                right = middle - 1
            else:
                left = middle + 1

    return found


def main():
    data = [5, 32, 41, 58, 132, 146, 178, 179, 230, 237]
    print('Data:', data)
    print('Is item in data?\n', binary_search(data, 146))
    print('Is item in data?\n', binary_search(data, 200))


if __name__ == "__main__":
    main()
