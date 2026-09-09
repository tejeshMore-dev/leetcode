# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        i = 0

        def helper(upper_bound):
            nonlocal i

            if i == len(preorder) or preorder[i] > upper_bound:
                return None
            
            node = TreeNode(preorder[i])
            i += 1

            node.left = helper(node.val)
            node.right = helper(upper_bound)

            return node
        
        return helper(float('inf'))
