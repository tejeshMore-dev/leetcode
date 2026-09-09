# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def helper(node):
            nonlocal ans

            if not node:
                return 0, 0
            
            left = helper(node.left)
            right = helper(node.right)

            left_count = 0
            right_count = 0
            
            if node.left:
                left_count = left[1] + 1
            
            if node.right:
                right_count = right[0] + 1
            
            ans = max(ans, left_count, right_count)

            return left_count, right_count
        
        helper(root)
        return ans
