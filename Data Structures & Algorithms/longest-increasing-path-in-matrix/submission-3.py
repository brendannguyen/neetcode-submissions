class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # Kahn's algorithm
        ROWS, COLS = len(matrix), len(matrix[0])
        indegree = [[0]*COLS for _ in range(ROWS)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # compute indegrees
        for r in range(ROWS):
            for c in range(COLS):
                for dx, dy in directions:
                    newR, newC = r+dy, c+dx
                    if (0 <= newR < ROWS and 0 <= newC < COLS and matrix[newR][newC] < matrix[r][c]):
                        indegree[r][c] += 1

        # add 0 indegree nodes to queue
        queue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if indegree[r][c] == 0:
                    queue.append((r, c))
        
        # bfs: pop first in queue, look at neighbours, -1 from each neighbour indegree, add neighbour to queue if indegree is now 0
        result = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dx, dy in directions:
                    newR, newC = r + dy, c + dx
                    if (0 <= newR < ROWS and 0 <= newC < COLS and matrix[newR][newC] > matrix[r][c]):
                        indegree[newR][newC] -= 1
                        if indegree[newR][newC] == 0:
                            queue.append((newR, newC))
            
            result += 1

        return result