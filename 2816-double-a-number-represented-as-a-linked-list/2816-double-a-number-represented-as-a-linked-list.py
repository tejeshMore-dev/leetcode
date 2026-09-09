# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node):
            previous = None

            while node:
                temp = node.next
                node.next = previous
                previous = node
                node = temp

            return previous


        node = reverse(head)
        dummy = ListNode(-1)
        current = dummy
        carry = 0

        while node or carry:
            val = 0
            
            if node:
                val += node.val * 2
                node = node.next
            
            if carry:
                val += carry

            current.next = ListNode(val % 10)
            current = current.next
            carry = val // 10
            
        
        return reverse(dummy.next)