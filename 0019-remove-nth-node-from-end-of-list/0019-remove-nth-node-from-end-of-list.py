# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        slow = dummy
        fast = dummy
        
        while n:
            fast = fast.next
            n -= 1

        previous = dummy

        while fast:
            previous = slow
            slow = slow.next
            fast = fast.next
        
        previous.next = slow.next
        return dummy.next
