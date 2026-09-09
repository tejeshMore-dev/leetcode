# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        preorder_i = 0
        postorder_i = {
            val : i for i, val in enumerate(postorder)
        }

        def build(post_left, post_right):
            nonlocal preorder_i

            if post_left > post_right:
                return None

            root_val = preorder[preorder_i]
            root = TreeNode(root_val)
            preorder_i += 1

            if post_left == post_right:
                return root
            
            left_subtree_root_val = preorder[preorder_i]
            left_root_post_index = postorder_i[left_subtree_root_val]

            root.left = build(post_left, left_root_post_index)
            root.right = build(left_root_post_index + 1, post_right-1)

            return root
        
        return build(0, len(postorder) - 1)

