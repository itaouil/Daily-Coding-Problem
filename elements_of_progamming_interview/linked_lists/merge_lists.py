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

        #  Initialize pointer
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


def merge2(l1, l2):
    head = l1 if l1.data < l2.data else l2
    while l1 and l2:
        if l1.data < l2.data:
            l1.next, l1 = l2, l1.next
        else:
            l2.next, l2 = l1, l2.next
    return head


def create_linked_list(numbers):
    head = tail = ListNode()
    for number in numbers:
        tail.data = number
        tail.next = ListNode()
        tail = tail.next
    tail = None
    return head


def is_sorted(llist):
    tail = llist
    while tail.next:
        if tail.data > tail.next.data:
            return False
        tail = tail.next
    return True


class TestMerging(unittest.TestCase):
    def test_merging(self):
        assert is_sorted(merge2(
            create_linked_list([2, 5, 7]),
            create_linked_list([3, 11])))


import unittest
unittest.main()
