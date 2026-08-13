# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = deque([root])
        level = -1

        while queue:
            queue_length = len(queue)
            level += 1
            previous = None

            for i in range(queue_length):
                node = queue.popleft()

                #even
                if level % 2 == 0:
                    if node.val % 2 == 0:
                        return False

                    if previous and node.val <= previous:
                        return False

                #odd
                if level % 2 != 0:
                    if node.val % 2 != 0:
                        return False

                    if previous and node.val >= previous:
                        return False
                
                previous = node.val

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
        
        return True
        