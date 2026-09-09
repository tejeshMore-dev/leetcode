# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        tree_map = {}
        childrens = set()

        for parent, child, is_left in descriptions:
            if parent not in tree_map:
                tree_map[parent] = TreeNode(parent)

            if child not in tree_map:
                tree_map[child] = TreeNode(child)
                
            parent_node = tree_map[parent]
            child_node = tree_map[child]

            if is_left:
                parent_node.left = child_node
            else:
                parent_node.right = child_node

            childrens.add(child)

        for parent, _, _ in descriptions:
            if parent not in childrens:
                return tree_map[parent]

        return None

