# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        
        ans = []
        def helper(node, current):
            nonlocal ans

            if not node:
                return 

            if current:
                current += "->"
                
            current += str(node.val)

            if not node.left and not node.right:
                ans.append(current)
                return 
            
            helper(node.left, current)
            helper(node.right, current)

        helper(root, "")
        return ans