# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0

        def helper(node, current_max):
            nonlocal ans
            
            if not node:
                return
            
            if node.val >= current_max:
                ans += 1

            if not node.left and not node.right:
                return
            
            helper(node.left, max(current_max, node.val))
            helper(node.right, max(current_max, node.val))

        helper(root, -float('inf'))
        return ans
        