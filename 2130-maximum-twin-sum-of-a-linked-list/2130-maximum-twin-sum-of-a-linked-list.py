# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = slow.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        node = slow.next

        slow.next = None
        previous = None
        while node:
            temp = node.next
            node.next = previous
            previous = node
            node = temp

        tail = fast
        ans = 0
        while tail and head:
            ans = max(ans, head.val + tail.val)
            head = head.next
            tail = tail.next
        
        return ans



