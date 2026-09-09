# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def find_lca(node):
            if not node:
                return None
            
            if node.val == startValue or node.val == destValue:
                return node
            
            left = find_lca(node.left)
            right = find_lca(node.right)

            if left and right:
                return node
            
            return left or right
             
        def find_path(node, target, path):
            if not node:
                return False

            if node.val == target:
                return True

            path.append("L")
            if find_path(node.left, target, path):
                return True
            path.pop()

            path.append("R")
            if find_path(node.right, target, path):
                return True
            path.pop()

            return False
            
        lca = find_lca(root)

        start_path = []
        destination_path = []

        find_path(lca, startValue, start_path)
        find_path(lca, destValue, destination_path)

        upward_path = "U" * len(start_path)

        return upward_path + "".join(destination_path)


        


            
            