# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans = None
        queue = deque([root])

        while queue:
            queue_length = len(queue)
            
            for i in range(queue_length):
                node = queue.popleft()
                if i == 0:
                    ans = node.val

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
        
        return ans