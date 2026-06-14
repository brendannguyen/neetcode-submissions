class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
        queue = deque()
        freshCount = 0

        for x in range(COLS):
            for y in range(ROWS):
                if grid[y][x] == 2:
                    queue.append((x, y))
                    visited[y][x] = True
        
                if grid[y][x] == 1:
                    freshCount += 1
   
        if not queue and freshCount == 0:
            return 0
        if not queue and freshCount > 0:
            return -1
        
        def checkCell(x, y):
            if x < 0 or x >= COLS or y < 0 or y >= ROWS or grid[y][x] == 2 or visited[y][x]:
                return
            
            if grid[y][x] == 0:
                visited[y][x] = True
                return
            
            visited[y][x] = True
            queue.append((x, y))


        level = 0
        while queue:
            for i in range(len(queue)):
                x, y = queue.popleft()

                checkCell(x+1, y)
                checkCell(x-1, y)
                checkCell(x, y+1)
                checkCell(x, y-1)

            level += 1

        print(visited)

        for x in range(len(visited[0])):
            for y in range(len(visited)):
                if not visited[y][x]:
                    return -1

        return level-1
