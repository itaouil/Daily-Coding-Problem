import random
import math


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def create_random_tree(number_of_nodes, root, chance_of_left=0.5):
    if not number_of_nodes: return root
    if random.random() < chance_of_left:
        root.left = BinaryTreeNode(random.randint(1, 100))
        create_random_tree(number_of_nodes - 1, root.left, chance_of_left)
    else:
        root.right = BinaryTreeNode(random.randint(1, 100))
        create_random_tree(number_of_nodes - 1, root.right, chance_of_left)


root = BinaryTreeNode(5)
root.left = BinaryTreeNode(1)
root.left.right = BinaryTreeNode(5)
root.left.right.left = BinaryTreeNode(1)


def depth(root):
    if not root: return 0
    if not root.left and not root.right:
        return 0
    if not root.left:
        return 1 + depth(root.right)
    else:
        return 1 + depth(root.left)


def is_height_balanced(root):
    return abs(depth(root.right) - depth(root.left)) <= 1


print(is_height_balanced(root))


# TODO: add tests