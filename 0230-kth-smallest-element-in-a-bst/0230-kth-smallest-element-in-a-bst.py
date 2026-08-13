# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = None

        def helper(node):
            nonlocal k, ans
            
            if not node:
                return False
            
            if helper(node.left):
                return True
            
            k -= 1
            if k == 0:
                ans = node.val
                return True
            
            if helper(node.right):
                return True
        
        helper(root)
        return ans