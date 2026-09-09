# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        num_i = {
            num : i for i, num in enumerate(nums)
        }

        def build(l, r):
            if l > r:
                return None

            max_val = max(nums[l:r + 1])
            max_i = num_i[max_val]

            node = TreeNode(max_val)
            node.left = build(l, max_i - 1)
            node.right = build(max_i + 1, r)

            return node

        return build(0, len(nums) - 1) 
        