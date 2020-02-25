"""
    This problem was asked by Uber.

    Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

    For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

    Follow-up: what if you can't use division?

    Solution:
        - Time: O(N)
        - Memory: O(N)
"""

import unittest

def array_product(A):
    # Invalid input
    if not A or len(A) < 2:
        return []

    # Store array length
    n = len(A)

    # Left and Right
    # product list
    left = []
    right = []

    # Compute left product values
    for x in range(n):
        # If first number
        # just add 1
        if(x == 0):
            left.append(1)
        else:
            left.append(A[x-1] * left[-1])

    # Compute right product values
    for x in range(n, 0, -1):
        # If first number
        # just add 1
        if(x == n):
            right.append(1)
        else:
            right.append(A[x] * right[-1])

    # Reverse right product list
    right.reverse()

    # Compute new product list
    result = [right[x] * left[x] for x in range(n)]

    return result

class TestArrayProduct(unittest.TestCase):

    def test_invalid_input(self):
        self.assertEqual([], array_product([]))
        self.assertEqual([], array_product([2]))
        self.assertEqual([], array_product(None))

    def test_array_product(self):
        self.assertEqual([24,30,40,60], array_product([5,4,3,2]))
        self.assertEqual([2,3,6], array_product([3,2,1]))
        self.assertEqual([120, 60, 40, 30, 24], array_product([1, 2, 3, 4, 5]))

if __name__ == "__main__":
    unittest.main()
