# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        ans = 0
        queue = deque([(root, 0)])

        while queue:
            queue_length = len(queue)
            first_index = queue[0][1]

            for _ in range(queue_length):
                node, index = queue.popleft()
                last_index = index

                if node.left:
                    queue.append((node.left, 2*index + 1))
                
                if node.right:
                    queue.append((node.right, 2*index + 2))

            ans = max(ans, last_index - first_index + 1)
        
        return ans