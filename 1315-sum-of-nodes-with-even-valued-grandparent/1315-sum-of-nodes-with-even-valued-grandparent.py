# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        path = []
        ans = 0

        def helper(node):
            nonlocal ans
            
            if not node:
                return
            
            path.append(node.val)

            if len(path) >= 3 and path[-3] % 2 == 0:
                ans += node.val

            helper(node.left)
            helper(node.right)
            path.pop()
        
        helper(root)
        return ans
