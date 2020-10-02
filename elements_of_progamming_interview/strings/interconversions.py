"""
    Problem 6.1.

    Solution:
        - Time: O(N)
        - Space: O(1)
"""

import string
import unittest

def int_to_string(x):
    # Array of single numbers
    result = []

    # Negative flag
    negative = False

    # Check if x negative
    if x < 0:
        negative = True
        x *= -1

    while x:
        result.append(string.digits[x % 10])

        # Update x
        x //= 10

    # Handle negative case
    if negative:
        result.append('-')
        
    return ''.join(reversed(result))

def string_to_int(s):
    # Final result
    result = 0

    # Iterate over string
    for i, x in enumerate(reversed(s[s[0] == '-':])):
        # Update result
        result += ((10 ** i) * string.digits.index(x))
        
    return result if s[0] != '-' else result * -1

class TestPartition(unittest.TestCase):

    def test_int_to_string(self):
        self.assertEqual("320", int_to_string(320))
        self.assertEqual("450", int_to_string(450))
        self.assertEqual("-378", int_to_string(-378))
        self.assertEqual("-1", int_to_string(-1))

    def test_string_to_int(self):
        self.assertEqual(320, string_to_int("320"))
        self.assertEqual(450, string_to_int("450"))
        self.assertEqual(-378, string_to_int("-378"))
        self.assertEqual(-1, string_to_int("-1"))

if __name__ == "__main__":
    unittest.main()
