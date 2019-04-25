"""
    Given an array of integers, return a new array such that each element at index i
    of the new array is the product of all the numbers in the original array except
    the one at i.

    For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
    If our input was [3, 2, 1], the expected output would be [2, 3, 6].

    Complexities:
        - Time: O(N)
        - Space: O(N)
"""

import unittest

def array_product(A):
    if not A:
        return None

    # Left product
    left_prod = []

    # Right product
    right_prod = []

    # Populate left product
    for x in range(len(A)):
        if x == 0:
            left_prod.append(1)
        else:
            left_prod.append(left_prod[x-1] * A[x-1])

    # Populate right product
    for x in range(len(A)-1, -1, -1):
        if x == len(A)-1:
            right_prod.append(1)
        else:
            right_prod.append(right_prod[-1] * A[x+1])

    # Reverse right production
    right_prod = right_prod[::-1]

    # Combine left and right products
    prod = []
    for x in range(len(A)):
        prod.append(left_prod[x] * right_prod[x])

    return prod

class TestArrayProduct(unittest.TestCase):

    def test_empty_input(self):
        self.assertEqual(None, array_product([]))

    def test_array_product(self):
        self.assertEqual([120, 60, 40, 30, 24], array_product([1, 2, 3, 4, 5]))

if __name__ == "__main__":
    unittest.main()
