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


def depth(root):
    if not root: return 0
    if not root.left and not root.right:
        return 0
    if not root.left:
        return 1 + depth(root.right)
    else:
        return 1 + depth(root.left)


def is_height_balanced(tree, current_height=0):
    if tree is None:
        return True, current_height - 1
    elif tree.left is None and tree.right is None:
        return True, current_height

    balanced_left, height_left = is_height_balanced(tree.left, current_height + 1)
    balanced_right, height_right = is_height_balanced(tree.right, current_height + 1)
    height = max(height_left, height_right)

    if balanced_left and balanced_right:
        return (abs(height_left - height_right) <= 1), height
    else:
        return False, height


def test_height_balance():
    tree = BinaryTreeNode(5)
    tree.left = BinaryTreeNode(1)
    tree.left.right = BinaryTreeNode(5)
    tree.left.right.left = BinaryTreeNode(1)
    balanced, height = is_height_balanced(tree)
    assert not balanced
    assert height == 3
