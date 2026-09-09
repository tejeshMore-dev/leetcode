# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        ans = []
        queue = deque([root])

        while queue:
            queue_length = len(queue)
            maximum = -float('inf')

            for i in range(queue_length):
                node = queue.popleft()
                maximum = max(maximum, node.val)

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            ans.append(maximum)
        
        return ans