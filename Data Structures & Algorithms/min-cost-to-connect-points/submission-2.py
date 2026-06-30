class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Prims algorithm in O(n^2), computing distances as we go instead of adj list
        # can also use adj matrix with space O(n^2)
        n = len(points)
        dist = [float('inf')]*n 
        dist[0] = 0
        visited = set()
        result = 0
        currNode = 0

        while len(visited) < n:
            visited.add(currNode)
            nextNode = -1
            for i in range(n):
                if i in visited:
                    continue
                x1, y1 = points[currNode]
                x2, y2 = points[i]
                distance = abs(x1-x2) + abs(y1-y2)
                dist[i] = min(dist[i], distance)

                # getting next min distance edge
                if nextNode == -1 or dist[i] < dist[nextNode]:
                    nextNode = i
            
            result += dist[currNode]
            currNode = nextNode

        return result