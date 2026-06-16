class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        neighbours = {}

        for i in range(n):
            neighbours[i] = []
        
        for n1, n2 in edges:
            neighbours[n1].append(n2)
            neighbours[n2].append(n1)
    
        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)
            for neighbour in neighbours[node]:
                if neighbour == parent:
                    continue
                if not dfs(neighbour, node):
                    return False
            
            return True

        return dfs(0, -1) and len(visited) == n