# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        ans = float('inf')
        previous = None

        def helper(node):
            nonlocal previous
            nonlocal ans

            if not node:
                return 

            helper(node.left)
            if previous is not None:
                ans = min(ans, abs(node.val - previous))
            
            previous = node.val
            helper(node.right)

        helper(root)        
        return ans