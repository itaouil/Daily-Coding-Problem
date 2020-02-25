"""
    This problem was recently asked by Google.

    Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

    For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

    Bonus: Can you do this in one pass?

    Solution:
        - Time: O(N)
        - Space: O(N)
"""

import unittest

def sum_to_k(A, k):
    # Invalid input
    if not A or len(A) < 2:
        return False

    # Create dictionary
    map = set()

    # Iterate over
    # list elements
    for a in A:
        # Compute k difference
        diff = k - a

        # Check if diff is < 0
        if(diff < 0):
            continue

        # Check if diff exists
        # in the map
        if diff in map:
            return True
        else:
            map.add(a)

    # If not match found
    # no existing solution
    return False

class TestSumToK(unittest.TestCase):

    def test_empty_input(self):
        self.assertEqual(False, sum_to_k(None, 0))
        self.assertEqual(False, sum_to_k([], 0))
        self.assertEqual(False, sum_to_k([9], 0))

    def test_sum_to_k(self):
        self.assertEqual(True, sum_to_k([1, 2, 3, 4, 5], 6))
        self.assertEqual(True, sum_to_k([10, 15, 3, 7], 17))
        self.assertEqual(False, sum_to_k([10, 15, 3, 7], 20))

if __name__ == "__main__":
    unittest.main()
