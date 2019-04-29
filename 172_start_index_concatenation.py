"""
    Given a string s and a list of words words, where each word is the same length, find all starting indices of substrings in s that is a concatenation of every word in words exactly once.

    For example, given s = "dogcatcatcodecatdog" and words = ["cat", "dog"], return [0, 13], since "dogcat" starts at index 0 and "catdog" starts at index 13.

    Given s = "barfoobazbitbyte" and words = ["dog", "cat"], return [] since there are no substrings composed of "dog" and "cat" in s.

    The order of the indices does not matter.
"""

import unittest

def find_starting_indeces(s, words):
    # Invalid input
    if not s or not words:
        return []

    # String length
    s_len = len(s)

    # Word length
    w_len = len(words[0])

    # Number of words
    n_words = len(words)

    # Hash map word/counter
    h_words = set(words)

    # Words that are seen
    seen = set()

    # Counter for seen words so far
    count = 0

    # Start index of the subtring
    start = 0

    # Output result
    result = []

    # Iterate over string using pointers
    ind = 0
    while ind < s_len:
        # String substring word
        word = s[ind:ind+w_len]

        # Word not in words list
        if word not in h_words:
            count = 0
            seen = set()

            # Move till next valid word
            while ind < s_len and s[ind:ind+w_len] not in h_words:
                ind += 1

            continue

        # Word in word list but seen
        if word in seen:
            count = 0
            seen = set()
            ind += 3
            continue

        # Word in list and not seen before and not all word seen yet
        if word in h_words and word not in seen:
            # Increase counter
            count += 1

            # Check if all words seen
            if count == 1:
                start = ind
                seen.add(word)
            elif count < n_words:
                seen.add(word)
            else:
                count = 0
                seen = set()
                result.append(start)

            # Increase pointer index
            ind += 3

    return result

class TestIndexConcatenation(unittest.TestCase):
    def test_0(self):
        self.assertEqual([], find_starting_indeces("", ["cat", "dog"]))

    def test_1(self):
        self.assertEqual([0, 13], find_starting_indeces("dogcatcatcodecatdog", ["cat", "dog"]))

    def test_2(self):
        self.assertEqual([], find_starting_indeces("barfoobazbitbyte", ["cat", "dog"]))

# Run tests
if __name__ == "__main__":
    unittest.main()
