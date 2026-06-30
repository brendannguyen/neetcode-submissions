class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # prims algorithm

        # create adjList
        # calculating dist from point to every point O(n^2)
        n = len(points)
        adjList = {i:[] for i in range(n)}
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adjList[i].append((dist, j))
                adjList[j].append((dist, i))
        
        result = 0
        visited = set()
        minHeap = [(0, 0)]

        # O(n^2logn) - logn for min heap
        while len(visited) < n:
            dist, i = heapq.heappop(minHeap)
            if i in visited:
                continue
            
            visited.add(i)
            result += dist

            for nextDist, j in adjList[i]:
                if j not in visited:
                    heapq.heappush(minHeap, (nextDist, j))

        return result
