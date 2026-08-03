# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        node = slow.next
        slow.next = None
        prev = None
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        
        node1 = head
        node2 = prev
        
        while node1 and node2:
            temp = node1.next
            node1.next = node2
            temp2 = node2.next
            node2.next = temp

            node1 = temp
            node2 = temp2
    