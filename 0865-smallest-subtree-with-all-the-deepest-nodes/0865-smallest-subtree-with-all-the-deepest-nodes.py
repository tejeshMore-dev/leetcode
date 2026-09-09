# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node):
            if not node:
                return None, 0

            left_lca, left_depth = helper(node.left)
            right_lca, right_depth = helper(node.right)

            if left_depth == right_depth:
                return node, 1 + left_depth
            elif left_depth > right_depth:
                return left_lca, 1 + left_depth
            else:
                return right_lca, 1 + right_depth

        
        lca, _ = helper(root)
        return lca
