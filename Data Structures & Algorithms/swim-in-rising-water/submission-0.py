class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # dijkstras algorithm
        # adjList / matrix, 

        # priority queue (minheap)
        # while queue
        # get min
        # look at neighbours (adjust distances)
        # add to queue if not visited

        n = len(grid)
        visited = set()
        minHeap = [(grid[0][0], 0, 0)]
        visited.add((0, 0))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        result = 0

        while minHeap:
            d, x, y = heapq.heappop(minHeap)
            if x == n-1 and y == n-1:
                result = d

            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    heapq.heappush(minHeap, (max(grid[ny][nx], d), nx, ny))

        return result
