# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def helper(node):
            if not node:
                return 0
            
            if node.val < low:
                return helper(node.right)

            if node.val > high:
                return helper(node.left)
            

            return (
                node.val
                + helper(node.left)
                + helper(node.right)
            )

        return helper(root)        
