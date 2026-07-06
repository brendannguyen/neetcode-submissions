class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # include it if increasing
        # up, down, left, right

        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [[-1]*COLS for _ in range(ROWS)]

        def dfs(r, c,  currentCount):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return 0
            
            if dp[r][c] != -1:
                return dp[r][c]
            
            result = 0
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                newR, newC = r+dy, c+dx

                if (0 <= newR < ROWS) and (0 <= newC < COLS) and (matrix[newR][newC] > matrix[r][c]):
                    result = max(result, dfs(newR, newC, currentCount))
            
            dp[r][c] = result + 1
            return dp[r][c]

        result = 0
        for r in range(ROWS):
            for c in range(COLS):
                result = max(result, dfs(r,c,0))
        return result
        