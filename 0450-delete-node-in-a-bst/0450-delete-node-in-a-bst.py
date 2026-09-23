# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        def helper(node, key):
            if not node:
                return None
            
            if key == node.val:
                if not node.left and not node.right:
                    return None

                elif node.right:
                    succesor = node.right

                    while succesor and succesor.left:
                        succesor = succesor.left
                    
                    node.val = succesor.val
                    node.right = helper(node.right, succesor.val)

                elif node.left:
                    prodecessor = node.left

                    while prodecessor and prodecessor.right:
                        prodecessor = prodecessor.right
                    
                    node.val = prodecessor.val
                    node.left = helper(node.left, prodecessor.val)

            elif key < node.val:
                node.left = helper(node.left, key)
            else:
                node.right = helper(node.right, key)
            
            return node

        return helper(root, key)
