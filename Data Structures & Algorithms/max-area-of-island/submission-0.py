class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        COLS, ROWS = len(grid[0]), len(grid)
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

        def dfs(x, y):
            if x >= COLS or x < 0 or y >= ROWS or y < 0 or grid[y][x] == 0 or visited[y][x]:
                return 0
            
            visited[y][x] = True

            return (
                dfs(x+1, y) +
                dfs(x-1, y) +
                dfs(x, y+1) +
                dfs(x, y-1) + 1
            )
        
        for y in range(ROWS):
            for x in range(COLS):
                if not visited[y][x] and grid[y][x] != 0:
                    # dfs(x, y)
                    result = max(dfs(x, y), result)

        return result