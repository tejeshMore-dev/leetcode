# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_i = {
            val : i for i, val in enumerate(inorder)
        }
        n = len(postorder)
        postorder_i = n - 1

        def build(l, r):
            nonlocal postorder_i

            if l > r or postorder_i < 0:
                return None
            
            node = TreeNode(postorder[postorder_i])
            mid = inorder_i[postorder[postorder_i]]
            postorder_i -= 1
            
            node.right = build(mid+1, r)
            node.left = build(l, mid-1)

            return node

        return build(0, n-1)
