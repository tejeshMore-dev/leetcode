# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        last_seen = {}
        prefix_sum = 0

        node = dummy
        while node:
            prefix_sum += node.val
            last_seen[prefix_sum] = node

            node = node.next
        
        prefix_sum = 0
        node = dummy
        while node:
            prefix_sum += node.val
            node.next  = last_seen[prefix_sum].next
            node = node.next

        return dummy.next

        