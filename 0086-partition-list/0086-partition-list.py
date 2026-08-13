# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smaller = ListNode(-101)
        higher = ListNode(-101)
        first_higher = higher
        first_smaller = smaller

        node = head

        while node:
            if node.val < x:
                smaller.next = node
                smaller = node
            else:
                higher.next = node
                higher = node
            
            node = node.next

        smaller.next = first_higher.next
        higher.next = None

        return first_smaller.next
        