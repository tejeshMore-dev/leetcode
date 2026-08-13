# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([root])
        min_depth = 0

        while queue:
            length = len(queue)
            min_depth += 1

            for _ in range(length):
                node = queue.popleft()

                if not node.left and not node.right:
                    return min_depth
                
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return min_depth
        # if not root:
        #     return 0
        
        # def helper(node):
        #     if not node:
        #         return float('inf')

        #     if not node.left and not node.right:
        #         return 1
        
        #     return min(helper(node.left), helper(node.right)) + 1
        
        # return helper(root)