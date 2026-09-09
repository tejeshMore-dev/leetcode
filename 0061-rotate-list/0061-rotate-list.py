# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head:
            return head

        n = 0 
        node = head  
        while node:
            n += 1
            old_right = node
            node = node.next
        
        k = k % n
        if k == 0:
            return head
        
        # old_left new_right  new_left old_right
        
        old_left = head
        slow = head
        fast = head

        while k:
            fast = fast.next
            k -= 1
        

        while fast.next:
            slow = slow.next
            fast = fast.next


        new_right = slow        
        new_left = slow.next

        slow.next = None
        old_right.next = old_left
        return new_left