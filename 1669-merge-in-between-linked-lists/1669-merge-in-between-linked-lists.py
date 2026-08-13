# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy = ListNode(-1, list1)
        previous = dummy
        slow = list1
        fast = list1
        diff = b - a

        while diff:
            fast = fast.next
            diff -= 1
        

        while fast and a:
            previous = slow
            slow = slow.next
            fast = fast.next

            a -= 1
        
        print(slow.val, fast.val, previous.val)
        previous.next = list2

        node = list2
        while node.next:
            node = node.next
        
        if fast and fast.next:
            node.next = fast.next

        return dummy.next

