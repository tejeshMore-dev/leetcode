# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        start = head
        mid = slow.next
        slow.next = None

        
        start = self.sortList(start)
        mid = self.sortList(mid)

        dummy = ListNode()
        tail = dummy       

        while start and mid:
            if start.val <= mid.val:
                tail.next = start
                start = start.next
            else:
                tail.next = mid
                mid = mid.next
            
            tail = tail.next
        
        tail.next = start if start else mid
        
        return dummy.next




        