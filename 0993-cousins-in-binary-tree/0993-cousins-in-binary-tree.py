# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = deque([(root, -1)])
        depth = 0

        while queue:
            queue_length = len(queue)
            x_present = False
            y_present = False
            depth += 1

            for _ in range(queue_length):
                node, parent = queue.popleft()

                if node.val == x:
                    x_present = True
                    x_parent = parent

                if node.val == y:
                    y_present = True
                    y_parent = parent
                
                if node.left:
                    queue.append((node.left, node))
                
                if node.right:
                    queue.append((node.right, node))
            
            if x_present and y_present and x_parent != y_parent:
                return True
        
        return False