class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # include it if increasing
        # up, down, left, right

        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [[-1]*COLS for _ in range(ROWS)]

        def dfs(r, c, prev):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or matrix[r][c] <= prev:
                return 0
            
            if dp[r][c] != -1:
                return dp[r][c]
            
            result = 0
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                newR, newC = r+dy, c+dx
                result = max(result, dfs(newR, newC, matrix[r][c]))
            
            dp[r][c] = result + 1
            return dp[r][c]

        result = 0
        for r in range(ROWS):
            for c in range(COLS):
                result = max(result, dfs(r,c,-1))
        return result
        