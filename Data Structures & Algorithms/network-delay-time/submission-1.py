class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adjList = {}
        dist = [float('inf')]*n
        visited = [False]*n
        dist[k-1] = 0

        for i in range(n):
            adjList[i] = []
        
        for u, v, t in times:
            adjList[u-1].append((v-1, t))
        
        minHeap = [(0, k-1)]

        while minHeap:
            curTime, curNode = heapq.heappop(minHeap)
            if visited[curNode]:
                continue
            
            visited[curNode] = True
            for v, t in adjList[curNode]:
                if dist[curNode] + t < dist[v]:
                    dist[v] = dist[curNode] + t
                    heapq.heappush(minHeap, (dist[v], v))
        
        return -1 if False in visited else max(dist)