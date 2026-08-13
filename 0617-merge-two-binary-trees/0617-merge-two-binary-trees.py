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
            
            merge_sum = 0
            if p:
                merge_sum += p.val
            
            if q:
                merge_sum += q.val
            
            new_node = TreeNode(merge_sum)

            if not p:
                left = helper(None, q.left)
                right = helper(None, q.right)
            elif not q:
                left = helper(p.left, None)
                right = helper(p.right, None)
            else:
                left = helper(p.left, q.left)
                right = helper(p.right, q.right)


            new_node.left, new_node.right = left, right

            return new_node
        
        return helper(root1, root2)