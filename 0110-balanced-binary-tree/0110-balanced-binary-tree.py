# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def helper(node):
            if not node:
                return 0, True
            
            left_h, left_r = helper(node.left)
            right_h, right_r = helper(node.right)

            if not left_r or not right_r:
                return 0, False
            
            if abs(left_h - right_h) > 1:
                return 0, False
            
            return 1 + max(left_h, right_h), True
        
        return helper(root)[1] 