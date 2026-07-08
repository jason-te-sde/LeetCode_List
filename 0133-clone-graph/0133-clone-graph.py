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

        """
            tag : graph
            tc. : O(n)
            sc. : O(n)
        """
        if node is None:
            return None
        visited = {}

        def dfs(node):
            if node in visited:
                return visited[node]
            else:
                new_val = node.val
                new_neighbors = []
                new_node = Node(new_val, new_neighbors)
                visited[node] = new_node

                for neighbor in node.neighbors:
                    new_node.neighbors.append(dfs(neighbor))

            return new_node
        
        return dfs(node)

                
            
