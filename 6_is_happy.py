"""
Write an algorithm to determine if a number n is "happy".

Starting with any positive integer, replace the number 
by the sum of the squares of its digits, and repeat the 
process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.
"""

import unittest

def digit_sum(n: int) -> int:
    # Digit sum
    sum_ = 0

    # Compute sum as
    # sum of digit squares
    while (n):
        # Get digit
        digit = n % 10

        # Update number
        n //= 10

        # Update sum
        sum_ += (digit * digit)
    
    return sum_

def is_happy(n: int) -> bool:
    # Unordered set
    seen = set()

    while (True):
        # Compute sum of squares
        n = digit_sum(n)

        # Check loop
        if n in seen:
            return False
        
        # Update set
        seen.add(n)

        # Check if number is happy
        if n == 1:
            return True

class TestHappiness(unittest.TestCase):
    def test_working(self):
        self.assertEqual(True, is_happy(19))

if __name__ == "__main__":
    unittest.main() 