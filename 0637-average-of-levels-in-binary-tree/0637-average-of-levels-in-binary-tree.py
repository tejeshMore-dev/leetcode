# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        ans = []
        queue = deque([root])
        
        while queue:
            queue_length = len(queue)
            level_sum = 0
            level_count = 0
            
            for _ in range(queue_length):
                node = queue.popleft()
                level_sum += node.val
                level_count += 1

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
                    
            ans.append(level_sum/level_count)
        
        return ans