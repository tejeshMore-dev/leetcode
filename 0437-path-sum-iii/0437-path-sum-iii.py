# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_sum = {
            0 : 1
        }

        def helper(node, current_sum):
            if not node:
                return 0
            
            current_sum += node.val            
            ans = prefix_sum.get(current_sum - targetSum, 0)
            
            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1

            ans += helper(node.left, current_sum)
            ans += helper(node.right, current_sum)

            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) - 1

            return ans

        return helper(root, 0)

        # ans = 0

        # def helper(node, path_sums):
        #     nonlocal ans

        #     if not node:
        #         return

        #     new_path_sums = [ node.val ]

        #     if node.val == targetSum:
        #         ans += 1
            
        #     for previous_sum in path_sums:
        #         new_sum = previous_sum + node.val

        #         if new_sum == targetSum:
        #             ans += 1
                
        #         new_path_sums.append(new_sum)
                
        #     helper(node.left, new_path_sums)
        #     helper(node.right, new_path_sums)

        # helper(root, [])
        # return ans
        