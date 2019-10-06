import heapq
from collections import Counter, namedtuple


class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def huffman_encode(string):
    queue = []
    for char, freq in Counter(string).items():
        queue.append((freq, len(queue), Leaf(char)))

    heapq.heapify(queue)

    count = len(queue)
    while len(queue) > 1:
        freq1, _count1, left = heapq.heappop(queue)
        freq2, _count2, right = heapq.heappop(queue)
        heapq.heappush(queue, (freq1 + freq2, count, Node(left, right)))
        count += 1

    code = {}
    if queue:
        [(_freq, count, root)] = queue
        root.walk(code, "")

    return code


def huffman_decode(string, code):
    chars_list = [char for char in string]
    decoded_string = ""
    while chars_list:
        if chars_list[0] in code.values():
            for l, cod in code.items():
                if cod == chars_list[0]: decoded_string += l
            del chars_list[0]
        else:
            chars_list[0] = (chars_list[0]) + (chars_list[1])
            del chars_list[1]
    return decoded_string


def main():
    string = input()
    code = huffman_encode(string)
    encoded = "".join(code[char] for char in string)
    print(len(code), len(encoded))
    for char in sorted(code):
        print("{}: {}".format(char, code[char]))
    print(encoded)


if __name__ == "__main__":
    main()
