"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        cloned = {
            node: Node(node.val)
        }

        stack = [ node ]

        while stack:
            current = stack.pop()

            for nei in current.neighbors:
                if nei not in cloned:
                    cloned[nei] = Node(nei.val)
                    stack.append(nei)
                
                cloned[current].neighbors.append(cloned[nei])

        return cloned[node]



            

        
        