class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        freshCount = 0

        for x in range(COLS):
            for y in range(ROWS):
                if grid[y][x] == 2:
                    queue.append((x, y))
        
                if grid[y][x] == 1:
                    freshCount += 1
        
        def checkCell(x, y):
            nonlocal freshCount
            if x < 0 or x >= COLS or y < 0 or y >= ROWS or grid[y][x] == 2 or grid[y][x] == 0:
                return
            
            queue.append((x, y))
            freshCount -= 1
            grid[y][x] = 2

        level = 0
        while queue and freshCount > 0:
            for i in range(len(queue)):
                x, y = queue.popleft()

                checkCell(x+1, y)
                checkCell(x-1, y)
                checkCell(x, y+1)
                checkCell(x, y-1)

            level += 1

        return level if freshCount == 0 else -1
