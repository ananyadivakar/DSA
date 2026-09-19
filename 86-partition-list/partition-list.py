# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)

        less = less_dummy
        greater = greater_dummy

        current = head

        while current:
            if current.val < x:
                less.next = current
                less = less.next
            else:
                greater.next = current
                greater = greater.next

            current = current.next

        # Connect the two lists
        less.next = greater_dummy.next

        # Important: end the greater list
        greater.next = None

        return less_dummy.next
        