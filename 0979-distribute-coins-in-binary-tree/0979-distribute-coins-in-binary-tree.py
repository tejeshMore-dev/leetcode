# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: TreeNode | None) -> int:
        def helper(node):
            if not node:
                return 0, 0 # balance, moves
            
            left_balance, left_moves = helper(node.left)
            right_balance, right_moves = helper(node.right)

            current_balance = left_balance + right_balance + node.val - 1

            return current_balance, abs(current_balance) + abs(left_moves) + abs(right_moves)
        
        return helper(root)[1]
        