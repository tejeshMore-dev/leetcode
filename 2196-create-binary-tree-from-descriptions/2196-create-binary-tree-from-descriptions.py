# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        tree_map = {}
        children = set()

        for description in descriptions:
            parent, child, is_left = description

            parent_node = tree_map.get(parent, TreeNode(parent))
            child_node = tree_map.get(child, TreeNode(child))
            children.add(child)

            if is_left:
                parent_node.left = child_node
            else:
                parent_node.right = child_node

            tree_map[parent] = parent_node
            tree_map[child] = child_node
        
        for parent, _, _ in descriptions:
            if parent not in children:
                root = parent

        return tree_map[root]

