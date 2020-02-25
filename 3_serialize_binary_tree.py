"""
    This problem was asked by Google.

    Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

    For example, given the following Node class

    class Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    The following test should pass:

    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'

    Solution:
        - Time: O(N)
        - Memory: O(N + M) where M are single nodes and leaves
"""

import unittest

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(node):
    # Invalid input
    if not node:
        return ""

    # List storing
    # nodes' values
    string_values = []

    # Helper node to
    # serialize tree
    def helper(node):
        # Add root node value
        string_values.append(node.val)

        # Check if left
        # node exists and
        # handle the None case
        if node.left:
            helper(node.left)
        else:
            string_values.append("None")

        # Check if right
        # node exists and
        # handle the None case
        if node.right:
            helper(node.right)
        else:
            string_values.append("None")

    # Calle helper function
    helper(node)

    # Return serialized string
    return ",".join(string_values)

def deserialize(string):
    # case for empty tree
    if string == "":
        return None

    # Convert the
    # string into a list
    array_values = string.split(",")
    print(array_values)

    # Helper function to
    # deserialize the string
    def helper(values, index=-1):
        # keep track
        # of the index
        index += 1

        # checker that return a None
        # value according to the string
        if values[index] == "None":
            return None

        # creation of the node and
        # initialization with its value
        # print(values[index])
        node = Node(
                    values[index],
                    helper(values, index),
                    helper(values, index)
               )

        return node

    # Calle helper function
    return helper(array_values)

class TestSerialize(unittest.TestCase):

    def test_invalid_input(self):
        self.assertEqual("", serialize(None))

    def test_serialize(self):
        self.assertEqual("root,left,left.left,None,None,None,right,None,None", serialize(Node('root', Node('left', Node('left.left')), Node('right'))))

    def test_deserialize(self):
        node = Node('root', Node('left', Node('left.left')), Node('right'))
        self.assertEqual('left', deserialize(serialize(node)).left.val)
        self.assertEqual('left.left', deserialize(serialize(node)).left.left.val)

if __name__ == "__main__":
    unittest.main()
