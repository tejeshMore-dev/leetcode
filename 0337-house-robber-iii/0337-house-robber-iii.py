# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode | None) -> int:
        def helper(node):
            if not node:
                return 0, 0 #broken, not_broken
            
            left_rob, left_no_rob = helper(node.left)
            right_rob, right_no_rob = helper(node.right)

            rob = node.val + left_no_rob + right_no_rob
            no_rob = max(left_rob + right_rob, left_no_rob + right_no_rob, left_rob + right_no_rob, right_rob + left_no_rob)

            return rob, no_rob
        
        rob, no_rob = helper(root)
        return max(rob, no_rob)