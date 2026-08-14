# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def helper(node, is_left):
            nonlocal ans
            
            if not node:
                return 
            
            if not node.left and not node.right:
                if is_left:
                    ans += node.val
                return
            
            helper(node.left, True)
            helper(node.right, False)
        
        helper(root, False)
        return ans