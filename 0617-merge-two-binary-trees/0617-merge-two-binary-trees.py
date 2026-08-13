# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(p, q):
            if not p and not q:
                return

            if not p:
                return q

            if not q:
                return p 
            
            merge_sum = p.val + q.val
            
            new_node = TreeNode(merge_sum)

            new_node.left, new_node.right = helper(p.left, q.left), helper(p.right, q.right)

            return new_node
        
        return helper(root1, root2)