"""
    This problem was asked by Stripe.

    Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

    For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

    You can modify the input array in-place.

    Solution:
        - Time: O(N)
        - Space: O(1)
"""

import unittest

def first_missing_positive(A):
    # Check if input is invalid
    if not A:
        return 1

    # If input valid then swap
    # numbers and position them
    # based on their index so that
    # we can maintain the linear time
    # constraint
    for i, num in enumerate(A):
        # Check that the number is
        # between 0 and len(A) and
        # that num is not already
        # in the correct position
        while i + 1 != num and 0 < num <= len(A):
            # Swap w.r.t target index
            # (which is num itself)
            A[i], A[num-1] = A[num-1], num

            # If we get a correspondence
            # break the while loop
            if A[i] == A[num-1]:
                break

    # Find missing positive integer
    for i, num in enumerate(A, 1):
        if i != num:
            return i

    return len(A) + 1

class TestFirstMissingPositive(unittest.TestCase):

    def test_invalid_input(self):
        self.assertEqual(1, first_missing_positive([]))
        self.assertEqual(1, first_missing_positive(None))

    def test_array_product(self):
        self.assertEqual(1, first_missing_positive([0,-1,-2,3]))
        self.assertEqual(3, first_missing_positive([0,1,2]))
        self.assertEqual(4, first_missing_positive([0,1,2,3,3,3,5]))

if __name__ == "__main__":
    unittest.main()
