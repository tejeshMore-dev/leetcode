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

        cloned_node_map = {}
        start = node.val
        visited = set([node.val])
        stack = [ node ]

        def get_cloned_node(val):
            if val not in cloned_node_map:
                cloned_node_map[val] = Node(val)

            return cloned_node_map[val]

        while stack:
            node = stack.pop()
            cloned_parent = get_cloned_node(node.val)

            for nei in node.neighbors:
                cloned_child = get_cloned_node(nei.val)
                cloned_parent.neighbors.append(cloned_child)

                if nei.val not in visited:
                    visited.add(nei.val)
                    stack.append(nei)
                
        
        return cloned_node_map[start]



            

        
        