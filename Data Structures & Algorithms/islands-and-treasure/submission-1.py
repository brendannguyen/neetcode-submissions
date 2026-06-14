class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        COLS, ROWS = len(grid[0]), len(grid)

        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
        queue = deque()

        for x in range(COLS):
            for y in range(ROWS):
                if grid[y][x] == 0:
                    queue.append((x,y))
                    visited[y][x] = True

        def addCell(x, y):
            if x < 0 or x >= COLS or y < 0 or y >= ROWS or grid[y][x] == -1 or visited[y][x]:
                return
            visited[y][x] = True
            queue.append((x, y))
        
        level = 0
        while queue:
            for i in range(len(queue)):
                x, y = queue.popleft()
                grid[y][x] = level

                addCell(x+1, y)
                addCell(x-1, y)
                addCell(x, y+1)
                addCell(x, y-1)

            level += 1
