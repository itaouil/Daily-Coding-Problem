"""
Given an integer array nums, find the contiguous 
subarray (containing at least one number) which 
has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

import unittest

def max_sub_array(A: list) -> int:
    best_sum = float('-inf')
    current_sum = 0

    for x in A:
        current_sum = max(x, current_sum + x)
        best_sum = max(best_sum, current_sum)

    return best_sum

class TestMaxSubArray(unittest.TestCase):

    def testMaxSubArray(self):
        self.assertEqual(6, max_sub_array([-2,1,-3,4,-1,2,1,-5,4]))

if __name__ == "__main__":
    unittest.main()