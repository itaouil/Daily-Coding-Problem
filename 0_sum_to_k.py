"""
    Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

    For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17

    Complexities:
        - Time: O(N)
        - Space: O(N)
"""

# Unit tests and math stuff
import math
import unittest

def sum_to_k(A, k):
    # Empty array
    if not A:
        return False

    # Difference set
    diff_set = set()

    # Find a match
    for x in A:
        if abs(x - k) in diff_set:
            return True
        else:
            diff_set.add(x)

    return False

"""
    Simple unit test for cross check.
"""
class TestSumToK(unittest.TestCase):

    def test_empty_input(self):
        self.assertEqual(False, sum_to_k([], 9))

    def test_sum_to_k_1(self):
        self.assertTrue(True, sum_to_k([10, 15, 3, 7], 17))

    def test_sum_to_k_2(self):
        self.assertFalse(False, sum_to_k([10, 1, 3, 7], 0))

if __name__ == '__main__':
    unittest.main()
