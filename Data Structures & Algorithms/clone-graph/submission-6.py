"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        seen = {}
        # seen[node] = Node(node.val)

        def dfs(cur):
            if cur in seen:
                return 
            
            seen[cur] = Node(cur.val)

            for neighbor in cur.neighbors:
                dfs(neighbor)
                seen[cur].neighbors.append(seen[neighbor])

        dfs(node)
        return seen[node]
