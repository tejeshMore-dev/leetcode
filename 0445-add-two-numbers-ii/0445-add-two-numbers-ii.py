# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(node):
            prev = None

            while node:
                temp = node.next
                node.next = prev
                prev = node
                node = temp
            
            return prev

        head1 = reverse(l1)
        head2 = reverse(l2)

        carry = 0
        dummy = ListNode(-1)
        current = dummy
        while head1 or head2 or carry:
            current_sum = 0

            if head1:
                current_sum += head1.val
                head1 = head1.next

            if head2:
                current_sum += head2.val
                head2 = head2.next

            if carry:
                current_sum += carry

            current.next = ListNode(current_sum % 10)
            current = current.next
            carry = current_sum // 10
        
        return reverse(dummy.next)

