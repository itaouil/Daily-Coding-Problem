"""
    This problem was asked by Airbnb.

    Given a list of words, find all pairs of unique indices such that the concatenation of the two words is a palindrome.

    For example, given the list ["code", "edoc", "da", "d"], return [(0, 1), (1, 0), (2, 3)].
"""

import unittest

def is_palindrome(word):
    return word == word[::-1]

# Brute force approach O(N^2 * C)
def naive_solution(words):
    # Result
    result = []

    # Iterate over words
    for i, word1 in enumerate(words):
        for j, word2 in enumerate(words):
            # Conutinue if same index
            if i == j:
                continue

            # Check if concatenation is palindrome
            if is_palindrome(word1, word2):
                result.append(i, j)

    return result

# Improved solution O(N * C^2)
def optimal_solution(words):
    if not words:
        return []

    # Set of words (word to index)
    d = {}
    for i, word in enumerate(words):
        d[word] = i

    # Find pairs
    result = []
    for i, word in enumerate(words):
        for char_i in range(len(word)):
            # Prefix and postfix
            prefix, postfix = word[:char_i], word[char_i:]

            # Reverse prefix and postfix
            reversed_prefix, reversed_postfix = prefix[::-1], postfix[::-1]

            # Postfix is a palindrome and prefix reversed in dictionary
            if is_palindrome(postfix) and reversed_prefix in d:
                if i != d[reversed_prefix]:
                    result.append((i, d[reversed_prefix]))

            # Prefix is a palindrome and postfix reversed in dictionary
            if is_palindrome(prefix) and reversed_postfix in d:
                if i != d[reversed_postfix]:
                    result.append((d[reversed_postfix], i))

    return result

class TestPalindromeConcatenation(unittest.TestCase):
    # Test empty input
    def test_empty_input(self):
        self.assertEqual([], optimal_solution([]))

    # Test case valid input
    def test_valid_input(self):
        self.assertEqual([(0, 1), (1, 0), (2, 3)], optimal_solution(["code", "edoc", "da", "d"]))

if __name__ == "__main__":
    unittest.main()
