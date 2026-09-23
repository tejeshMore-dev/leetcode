# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode | None) -> list[TreeNode | None]:
        node_path_map = defaultdict(list)
        ans = []
        used = set()

        def helper(node):
            if not node:
                return "None"
            
            left = helper(node.left)
            right = helper(node.right)

            path = str(node.val) + "-" + left + '-' + right
            
            if path in node_path_map[node.val] and path not in used:
                ans.append(node)
                used.add(path)

            node_path_map[node.val].append(path)
            return str(path)
        
        helper(root)
        return ans
        