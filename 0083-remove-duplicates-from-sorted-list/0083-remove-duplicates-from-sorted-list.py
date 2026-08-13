# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-101, head)
        current = head
        previous = dummy

        while current:
            if current.val == previous.val:
                previous.next = current.next
            else:
                previous = current
            
            current = current.next
        
        return dummy.next