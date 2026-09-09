# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def helper(node):
            nonlocal ans

            if not node:
                return 0
            
            left = helper(node.left)
            right = helper(node.right)

            left_count = 0
            right_count = 0

            if node.left and node.left.val == node.val:
                left_count = left + 1

            if node.right and node.right.val == node.val:
                right_count = right + 1
            
            ans = max(ans, left_count + right_count)

            return max(left_count, right_count)

        helper(root)
        return ans 
            