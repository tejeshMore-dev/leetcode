# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_i = { val: i for i, val in enumerate(inorder) }
        i = 0

        def build(l, r):
            nonlocal i

            if i == len(preorder) or l > r:
                return None
            
            node = TreeNode(preorder[i])
            middle = inorder_i[preorder[i]]
            i += 1

            node.left = build(l, middle - 1)
            node.right = build(middle + 1, r)

            return node
            
        return build(0, len(preorder))