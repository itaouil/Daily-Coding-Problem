import random


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def create_random_tree(number_of_nodes, root, chance_of_left=0.5):
    if not number_of_nodes: return root
    if random.random() < chance_of_left:
        root.left = BinaryTreeNode(random.randint(1, 100))
        create_random_tree(number_of_nodes-1, root.left, chance_of_left)
    else:
        root.right = BinaryTreeNode(random.randint(1, 100))
        create_random_tree(number_of_nodes-1, root.right, chance_of_left)

root = BinaryTreeNode(data=5)
t = create_random_tree(5, root)
print()


