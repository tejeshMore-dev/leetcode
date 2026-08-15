# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node):
            previous = None

            while node:
                temp = node.next
                node.next = previous
                previous = node
                node = temp

            return previous

        new_head = reverse(head)
        previous = new_head
        node = new_head.next

        while node:
            if node.val >= previous.val:
                previous.next = node
                previous = node

            node = node.next
        
        previous.next = None
        return reverse(new_head)