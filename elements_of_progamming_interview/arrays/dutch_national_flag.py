"""
    Problem 5.1.

    Solution:
        - Time: O(N)
        - Space: O(1)
"""

import unittest

def partition(A, idx):
    # Invalid input
    if A == None or idx == None:
        return None

    # Empty list
    if not A:
        return A

    # Define three pointers
    f, m, l = 0, 0, len(A) - 1

    # Current index
    i = 0

    # Pivot
    pivot = A[idx]

    while m <= l:
        if A[i] > pivot:
            # Swap with last element
            A[i], A[l] = A[l], A[i]

            # Decrease last element index
            l -= 1

        elif A[i] < pivot:
            # Swap with first middle element
            A[i], A[f] = A[f], A[i]

            # Increase pointer
            f, m =  f+1, m+1

            # Increase index
            i += 1

        # Case where element is same as pivot
        else:
            # Increase pointer
            m += 1

            # Increase index
            i += 1

    return A

class TestPartition(unittest.TestCase):

    def test_empty_input(self):
        self.partition(None, partition(None, 0))
        self.assertEqual(None, partition([], None))

    def test_partitioning(self):
        self.assertEqual([], partition([], 6))
        self.assertEqual([0,0,1,1,1,2,2], partition([0,1,2,0,2,1,1], 1))
        self.assertEqual([2,1,3,4,5,6], partition([2,1,3,4,5,6], 2))
        self.assertEqual([2,1,2,2,4,5,6,9], partition([2,1,2,2,5,9,4,6], 6))

if __name__ == "__main__":
    unittest.main()
