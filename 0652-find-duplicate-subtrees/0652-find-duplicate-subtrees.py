# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode | None) -> list[TreeNode | None]:
        pattern_frequency = defaultdict(int)
        ans = []

        def helper(node):
            if not node:
                return "#"
            
            left = helper(node.left)
            right = helper(node.right)

            pattern = str(node.val) + "-" + left + '-' + right
            pattern_frequency[pattern] += 1

            if pattern_frequency[pattern] == 2:
                ans.append(node)
        
            return pattern
        
        helper(root)
        return ans