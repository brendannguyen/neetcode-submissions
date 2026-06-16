class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # reach end and visited < n:
        # must be a connected component + 1

        visited = set()
        neighbours = {}

        for i in range(n):
            neighbours[i] = []
        for a, b in edges:
            neighbours[a].append(b)
            neighbours[b].append(a)
        
        def dfs(node):
            for neighbour in neighbours[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    dfs(neighbour)
        
        result = 0
        for node in range(n):
            if node not in visited:
                visited.add(node)
                dfs(node)
                result += 1
        
        return result