# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        INF = float('inf')

        def helper(node, l, r):
            if not node:
                return True
            
            if not ( l < node.val < r ):
                return False
            
            left = helper(node.left, l, node.val)
            right = helper(node.right, node.val, r)
            
            return left and right

        return helper(root, -INF, INF)