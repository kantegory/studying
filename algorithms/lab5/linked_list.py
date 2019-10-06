class Node:

    def __init__(self):
        self.data = None
        self.next = None

    def __str__(self):
        return "Data: %s, Next -> %s" % (self.data, self.next)


class LinkedList:
    def __init__(self):
        self.head = Node()
        self.curNode = self.head

    def insert_node(self, data):
        node = Node()
        node.data = data
        node.next = None

        if not self.head.data:
            self.head = node
            self.curNode = node
        else:
            self.curNode.next = node
            self.curNode = node

    def print(self):
        print(self.head)


if __name__ == "__main__":

    l = LinkedList()
    elems = []
    result = None
    number_of_elems = int(input('Введите количество элементов списка: '))

    for i in range(number_of_elems):
        elem = int(input('Введите элемент: '))
        l.insert_node(elem)
        elems.append(elem)

    l.print()

    for i in range(len(elems)):
        if elems[i] < elems[i -1]:
            result = False
        else:
            result = True

    print('Связный список отсортирован?\n', result)
