from tkinter import *
from math import *

# Создать структуру деревьев, построенную на списках, через класс
class Tree:
    def __init__(self, name='root', children=None):
        self.name = name
        self.children = []
        if children:
            for node in children:
                self.add_node(node)

    def __repr__(self):
        return self.name

    def add_node(self, node):
        self.children.append(node)


t = Tree('e', [Tree('b',
                    [Tree('a'), Tree('d',
                                     [Tree('c')])]),
               Tree('f',
                    [Tree('i',
                          [Tree('g',
                                [Tree('h')]), Tree('j')])])])


# Организовать вывод в консоль
def print_tree(Tree):
    print(Tree.name)
    for i in range(len(Tree.children)):
        if Tree.children[i]:
            print_tree(Tree.children[i])


# Организовать вывод в окошко в текстовом виде

# Организовать неупорядоченный граф. вывод в окошко

# Организовать упорядоченный граф. вывод в окошко


if __name__ == '__main__':
    print_tree(t)
