# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(node, current_max):
            if not node:
                return 0
            
            is_good = 0
            if node.val >= current_max:
                is_good += 1
            
            return (
                is_good
                + helper(node.left, max(current_max, node.val))
                + helper(node.right, max(current_max, node.val))
            )
            

        return helper(root, -float('inf'))        