# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        before = dummy
        slow = dummy
        fast = dummy

        diff = right - left
        while diff:
            fast = fast.next
            diff -= 1
        
        while left:
            before = slow
            slow = slow.next
            fast = fast.next

            left -= 1
        
        after = fast.next
        
        previous = None
        node = slow
        while node != after:
            temp = node.next
            node.next = previous
            previous = node
            node = temp
        
        before.next = fast
        slow.next = after

        return dummy.next
        