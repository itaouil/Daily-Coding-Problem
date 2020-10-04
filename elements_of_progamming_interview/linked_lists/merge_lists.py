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

def merge(L1, L2):
    # Cases
    if not L1 and not L2:
        return None
    elif L1 and not L2:
        return L1
    elif L2 and not L1:
        return L2
    else:
        # Initialize new LL
        dummy_head = tail = ListNode()

        # Merging process
        while L1 and L2:
            if L1.data <= L2.data:
                tail.next, L1 = L1, L1.next
            else:
                tail.next, L2 = L2, L2.next
            
            tail = tail.next
        
        # Add possible remaining
        # elements if list differ
        # in size
        tail = L1 or L2
        
        return dummy_head.next

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
