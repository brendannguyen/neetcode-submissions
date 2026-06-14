"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        # seen hash table
        # bfs/dfs and dont create new node if already seen (add to its neighbours)
        if not node:
            return None
        
        seen = {}
        seen[node] = Node(node.val)
        queue = deque([node])
        while queue:
            cur = queue.popleft()

            for neighbor in cur.neighbors:
                if neighbor not in seen:
                    seen[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                seen[cur].neighbors.append(seen[neighbor])
            
        return seen[node]