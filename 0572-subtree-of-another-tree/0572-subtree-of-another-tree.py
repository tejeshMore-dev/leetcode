# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(p, q):
            if not p and not q:
                return True
            
            if not p or not q:
                return False
            
            if p.val != q.val:
                return False
            
            return (
                check(p.left, q.left) 
                and check(p.right, q.right)
                )


        def helper(node):
            if not node:
                return False
            
            if node.val == subRoot.val and check(node, subRoot):
                return True

            return (
                helper(node.left) or
                helper(node.right)
            )
        
        if not subRoot:
            return True
            
        return helper(root)