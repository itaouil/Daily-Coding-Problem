"""
    Given an N by N matrix, rotate it by 90 degrees clockwise.

    For example, given the following matrix:

    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
    you should return:

    [[7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]]

    Complexities:
        - Time: O(N^2)
        - Space: O(N^2)

    Follow-up: What if you couldn't use any extra space?

    Complexities:
        - Time: O(N^2)
        - Space: O(1)
"""

import unittest

def is_square(M):
    return all(len(row) == len(M) for row in M)

def rotate_90_brute_force(M):
    if not M:
        return None

    # Check if matrix is square
    if not is_square(M):
        return None

    # New matrix
    result = [ [] for row in M ]

    # Update new matrix result
    for row in reversed(M):
        for i, item in enumerate(row):
            # Push item in correct position
            result[i].append(item)

    return result

def rotate_90_no_memory(M):
    if not M:
        return None

    # Check if matrix is square
    if not is_square(M):
        return None

    # Matrix size N
    n = len(M)

    # Iterate outer loop
    for x in range(n//2):
        # Last element
        last = n - x - 1
        count = 0
        #Inner loop
        for y in range(x, last):
            # Save right column
            right = M[y][last]

            # Save bottom
            bottom = M[last][last-count]

            # Move top to right
            M[y][last] = M[x][y]

            # Move right to bottom
            M[last][last-count] = right

            # Save left
            left = M[last-count][x]

            # Move bottom to left
            M[last-count][x] = bottom

            # Move left to top
            M[x][y] = left

            count += 1

    return M

class TestSubOptimal(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(None, rotate_90_brute_force([]))

    def test_rotation_brute_force(self):
        matrix = [ [1,2,3], [4,5,6], [7,8,9] ]
        outcome = [ [7,4,1], [8,5,2], [9,6,3] ]
        result = rotate_90_brute_force(matrix)
        self.assertEqual(outcome, result)

    def test_rotation(self):
        matrix = [ [1,2,3], [4,5,6], [7,8,9] ]
        outcome = [ [7,4,1], [8,5,2], [9,6,3] ]
        result = rotate_90_no_memory(matrix)
        self.assertEqual(outcome, result)

if __name__ == "__main__":
    unittest.main()
