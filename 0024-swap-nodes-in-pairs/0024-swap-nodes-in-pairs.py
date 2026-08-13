# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        previous = dummy

        while previous.next and previous.next.next:
            first = previous.next
            second = first.next

            first.next = second.next
            second.next = first
            previous.next = second

            previous = first

        return dummy.next
