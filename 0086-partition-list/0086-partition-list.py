# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        higher_dummy = ListNode(-101)
        smaller_dummy = ListNode(-101)
        higher = higher_dummy
        smaller = smaller_dummy

        node = head
        while node:
            if node.val < x:
                smaller.next = node
                smaller = node
            else:
                higher.next = node
                higher = node
            
            node = node.next

        smaller.next = higher_dummy.next
        higher.next = None

        return smaller_dummy.next
        