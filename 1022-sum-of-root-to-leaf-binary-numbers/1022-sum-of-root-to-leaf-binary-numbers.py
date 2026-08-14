# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        path = []
        ans = 0

        def helper(node):
            nonlocal ans

            if not node:
                return
            
            path.append(str(node.val))

            if not node.left and not node.right:
                num = int("".join(path), 2)
                ans += num
                path.pop()
                return 
            
            helper(node.left)
            helper(node.right)
            path.pop()

        helper(root)
        return ans
                