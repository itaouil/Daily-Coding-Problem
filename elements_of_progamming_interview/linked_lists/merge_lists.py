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
        merged = ListNode()

        # Initialize pointer
        pointer = merged

        # Merging process
        while l1 and l2:
            if l1.data <= l2.data:
                pointer.data = l1.data
                l1 = l1.next
            else:
                pointer.data = l2.data
                l2 = l2.next
            
            pointer = pointer.next
        
        # Check if any list was
        # shorter than the other
        if l1:
            pointer.data = l1.data
            pointer.next = l1.next
        elif l2:
            pointer.data = l2.data
            pointer.next = l2.next
        
        return merged