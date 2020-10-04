#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Problem 7.1.

    Solution:
        - Time: O(N + M)
        - Space: O(N + M)
"""

import unittest

# Node template
class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node

def merge(l1, l2):
    # Cases
    if not l1 and not l2:
        return None
    elif l1 and not l2:
        return l1
    elif l2 and not l1:
        return l2
    else:
        # Initialize new LL
        merged = ListNode(None, None)

        # Merging process
        while l1 and l2:
            if l1.data <= l2.data:
                merged.data = l1.data
                l1 = l1.next
            else:
                merged.data = l2.data
                l2 = l2.next
            
            merged.next = ListNode(None, None)
            merged = merged.next
        
        # Check if any list was
        # shorter than the other
        if l1:
            merged.data = l1.data
            merged.next = l1.next
        elif l2:
            merged.data = l2.data
            merged.next = l2.next
        
        return merged

# Create test case
list1 = ListNode(1, ListNode(3, ListNode(4, None)))
list2 = ListNode(0, ListNode(5, ListNode(6, None)))
list3 = ListNode(-5, ListNode(-3, ListNode(11, None)))

def is_sorted(llist):
    tail = llist
    while tail.next:
        if tail.data > tail.next.data:
            return False
        tail = tail.next
    return True

class TestMerge(unittest.TestCase):
    def testMergeCases(self):
        assert is_sorted(merge(list1, list2))
        assert is_sorted(merge(list3, list2))

if __name__ == "__main__":
    unittest.main()
