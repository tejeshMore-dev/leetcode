# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        i = 0
        ans = {}

        node = head
        while node:
            while stack and stack[-1][1] < node.val:
                smaller_i, _ = stack.pop()
                ans[smaller_i] = node.val

            stack.append([i, node.val])
            node = node.next
            i += 1
        
        n = i

        return [ ans.get(i, 0) for i in range(n) ]