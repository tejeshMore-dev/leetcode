# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -float('inf')
        max_level = 0

        queue = deque([root])
        level = 0

        while queue:
            queue_length = len(queue)
            level += 1
            current_sum = 0

            for i in range(queue_length):
                node = queue.popleft()
                current_sum += node.val

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            if current_sum > max_sum:
                max_level = level
                max_sum = current_sum
        
        return max_level