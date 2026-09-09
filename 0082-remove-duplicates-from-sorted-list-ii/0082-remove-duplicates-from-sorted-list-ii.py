# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-101, head)
        previous = dummy

        while previous.next and previous.next.next:
            first = previous.next
            second = first.next

            if first.val == second.val:
                node = second.next

                while node and node.val == second.val:
                    node = node.next
                
                if node:
                    previous.next = node
                else:
                    previous.next = None
                    break
            else:
                previous = first
        
        return dummy.next