# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        ans = []
        i = 0
         
        node = head
        while node:
            ans.append(0)

            while stack and stack[-1][1] < node.val:
                smaller_i, _ = stack.pop()
                ans[smaller_i] = node.val

            stack.append([i, node.val])

            node = node.next
            i += 1
    
        return ans