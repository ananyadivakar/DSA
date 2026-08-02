# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k == 0:
            return head

        # Find length and last node
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Reduce unnecessary rotations
        k = k % length
        if k == 0:
            return head

        # Make the list circular
        tail.next = head

        # Find new tail
        steps = length - k - 1
        new_tail = head
        while steps > 0:
            new_tail = new_tail.next
            steps -= 1

        # Break the circle
        new_head = new_tail.next
        new_tail.next = None

        return new_head