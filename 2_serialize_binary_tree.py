"""
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

    Complexities:
        - Time: O(N)
        - Space: O(N)
"""

# Unit test stuff
import unittest

# Node class definition
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Serialize function
def serialize(node):
    # Invalid tree
    if not node:
        return None

    # serialized list
    serialized_list = []

    # Traverse tree (node, left, right)
    def helper(node, side):
        # Base case
        if not node:
            serialized_list.append(str(side) + str(None))
            return

        # Append root
        serialized_list.append(str(side) + str(node.val))

        # Recursive calls to left
        # and right nodes
        helper(node.left, 'l')
        helper(node.right, 'r')

    # Serialize
    helper(node, 'ro')

    # Return serialized list
    return serialized_list

# Deserialize function
def deserialize(serialized_list):
    # Invalid tree
    if not serialized_list:
        return Node(None)

    # Deserialize first node (root)
    # and increase counter
    node = Node(serialized_list[0])
    count = 1

    # Traverse tree (node, left, right)
    def helper(node, count):
        # Serialized element
        val = serialized_list[count]

        if count == (len(serialized_list)-1):
            return

        if not node:
            return

        # Base case (left)
        if val[0] == 'l':
            if val[1:] == "None":
                node.left = None
                count += 1
                helper(node.left)
            else:
                node.left = val[1:]
                count += 1
                helper(node.left)

        # Base case (right)
        if val[0] == 'r':
            if val[1:] == "None":
                node.right = None
                count += 1
                helper(node.left)
            else:
                node.right = val[1:]
                count += 1
                helper(node.left)

    # Serialize
    helper(node, count)

    # Return serialized list
    return node

"""
    Assertion
"""
class TestSerialization(unittest.TestCase):

    def test_empty_input(self):
        self.assertEqual(None, serialize(Node(None)))

    def test_serialization(self):
        node = Node('root', Node('left', Node('left.left')), Node('right'))
        self.assertEqual('left.left', deserialize(serialize(node)).left.left.val)

if __name__ == "__main__":
    unittest.main()
# node = Node('root', Node('left', Node('left.left')), Node('right'))
# print(serialize(node))
