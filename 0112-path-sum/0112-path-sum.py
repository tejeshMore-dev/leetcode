# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(node, current_sum):
            if not node:
                return False

            current_sum += node.val

            if not node.left and not node.right:
                return current_sum == targetSum
            
            return (
                helper(node.left, current_sum)
                or helper(node.right, current_sum)
            )

        return helper(root, 0)    