"""
    Given a non-empty array of integers, every 
    element appears twice except for one. Find 
    that single one.

    Note:

    Your algorithm should have a linear runtime complexity. 
    Could you implement it without using extra memory?

    Example 1:

    Input: [2,2,1]
    Output: 1

    Example 2:

    Input: [4,1,2,1,2]
    Output: 4   
"""

import unittest

def linear_with_memory(A):
    """
        Find single number using
        hash set using a linear time
        and linear amount of memory.
    """
    if not A:
        return None
    
    if len(A) == 1:
        return A[0]
    
    seen = dict()

    for num in A:
        if num in seen:
            seen[num] += 1
        else:
            seen[num] = 1
    
    for (key, value) in seen.items():
        if value == 1: return key

def fully_linear(A):
    """
        Find single number using
        bit-wise operations in linear
        time completely.
    """
    if not A:
        return None
    
    if len(A) == 1:
        return A[0]

    x = A[0]

    for i in range(1, len(A)):
        x ^= A[i]
    
    return x

class TestSingleNumber(unittest.TestCase):

    def test_invalid_input(self):
        self.assertEqual(None, linear_with_memory(None))
        self.assertEqual(None, linear_with_memory([]))
        self.assertEqual(None, fully_linear(None))
        self.assertEqual(None, fully_linear([]))

    def test_working(self):
        self.assertEqual(1, linear_with_memory([2,2,1]))
        self.assertEqual(4, linear_with_memory([4,1,2,1,2]))
        self.assertEqual(1, fully_linear([2,2,1]))
        self.assertEqual(4, fully_linear([4,1,2,1,2]))

if __name__ == "__main__":
    unittest.main()