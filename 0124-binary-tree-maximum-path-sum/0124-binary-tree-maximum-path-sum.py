# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -float('inf')

        def helper(node):
            nonlocal ans

            if not node:
                return 0

            left = max(0, helper(node.left))
            right = max(0, helper(node.right))

            ans = max(ans, node.val + left + right)

            return max(left, right) + node.val
        
        helper(root)
        return ans