class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # dfs
        visited = set()
        neighbours = {}

        for i in range(1, len(edges)+1):
            neighbours[i] = []
        
        for n1, n2 in edges:
            neighbours[n1].append(n2)
            neighbours[n2].append(n1)

        cycle = set()
        cycleStart = -1

        def dfs(node, parent):
            nonlocal cycleStart
            if node in visited:
                cycleStart = node
                return True

            visited.add(node)
            for neighbour in neighbours[node]:
                if neighbour == parent:
                    continue
                if dfs(neighbour, node):
                    if cycleStart != -1:
                        cycle.add(node)
                    if node == cycleStart:
                        cycleStart = -1
                    return True
            
            return False

        dfs(1, -1)

        for i in range(len(edges)-1, -1, -1):
            a, b = edges[i]
            if a in cycle and b in cycle:
                return [a, b]

        return []