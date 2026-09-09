"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        ans = []

        while queue:
            queue_length = len(queue)
            level = []

            for _ in range(queue_length):
                node = queue.popleft()
                level.append(node.val)

                for child in node.children:
                    queue.append(child)
            
            ans.append(level)

        return ans