# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        def helper(left, right, level):
            if not left:
                return
            
            if level % 2 != 0:
                left.val, right.val = right.val, left.val

            helper(left.left, right.right, level + 1)
            helper(left.right, right.left, level + 1)

        helper(root.left, root.right, 1)
        return root

        # if not root:
        #     return root

        # queue = deque([root])
        # level = 0

        # while queue:
        #     queue_length = len(queue)

        #     num = [node.val for node in queue]

        #     for i in range(queue_length):
        #         node = queue.popleft()

        #         if level % 2 != 0:
        #             node.val = num[-1 - i]

        #         if node.left:
        #             queue.append(node.left)
                
        #         if node.right:
        #             queue.append(node.right)
            
        #     level += 1

            
        # return root