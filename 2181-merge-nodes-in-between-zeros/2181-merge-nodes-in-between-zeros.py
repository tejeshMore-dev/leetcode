# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        previous = dummy
        node = head.next
        current_sum = 0

        while node:
            if node.val == 0:
                previous.next = ListNode(current_sum)
                previous = previous.next
                current_sum = 0 
            else:
                current_sum += node.val
            
            node = node.next

        return dummy.next    
        