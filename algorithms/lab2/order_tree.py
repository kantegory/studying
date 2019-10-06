class Node:
    def __init__(self, data):
        self.left_child = None
        self.right_child = None
        self.data = data


def tree_insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.left_child is None:
                root.left_child = node
            else:
                tree_insert(root.left_child, node)
        else:
            if root.right_child is None:
                root.right_child = node
            else:
                tree_insert(root.right_child, node)


def inorder(root):
    if root.left_child is not None:
        inorder(root.left_child)
    print(root.data)
    if root.right_child is not None:
        inorder(root.right_child)


def backorder(root):
    if root.left_child is not None:
        backorder(root.left_child)
    if root.right_child is not None:
        backorder(root.right_child)
    print(root.data)


if __name__ == "__main__":
    root = Node(3)
    tree_insert(root, Node(11))
    tree_insert(root, Node(1))
    tree_insert(root, Node(13))
    tree_insert(root, Node(5))
    tree_insert(root, Node(17))
    tree_insert(root, Node(7))
    tree_insert(root, Node(19))
    print('Inorder:')
    inorder(root)
    print('Backorder:')
    backorder(root)
