# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        slow = dummy.next
        fast = slow

        previous = dummy
        while fast and fast.next:
            fast = fast.next
            temp = fast.next

            previous.next = fast
            fast.next = slow
            previous = slow
            previous.next = temp

            slow = temp
            fast = slow

        return dummy.next
