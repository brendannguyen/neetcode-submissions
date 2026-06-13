class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        result = 0
        COLS, ROWS = len(grid[0]), len(grid)
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
        print(visited)

        def dfs(x, y):
            if x >= COLS or x < 0 or y >= ROWS or y < 0 or grid[y][x] == '0' or visited[y][x]:
                return
            
            visited[y][x] = True

            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)
        
        for y in range(ROWS):
            for x in range(COLS):
                if not visited[y][x] and grid[y][x] != '0':
                    dfs(x, y)
                    result += 1
        print(visited)
        return result