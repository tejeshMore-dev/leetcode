# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        inorder_index_map = {}
        for i , num in enumerate(inorder):
            inorder_index_map[num] = i
        
        preorder_i = 0
        N = len(inorder)

        def build(l, r):
            nonlocal preorder_i

            if l > r:
                return None
            
            if preorder_i >= N:
                return None
            
            val = preorder[preorder_i]
            preorder_i += 1
            
            mid = inorder_index_map[val]
            root = TreeNode(val)

            root.left = build(l, mid - 1)
            root.right = build(mid + 1, r)

            return root

        return build(0, N)


        