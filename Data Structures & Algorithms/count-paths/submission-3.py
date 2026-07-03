class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # bottom up
        # dp[m][n] = unqiue paths from that point to bottom right corner
        # dp[m-1][n-1] = 


        # dp[m][n] = dp[m+1][n] + dp[m][n+1]

        # if m or n is out of bounds return 0
        # if m and n is bottom right, return 1

        memo = [[-1]*n for i in range(m)]

        def dfs(r, c):
            if r >= m or c >= n:
                return 0
            
            if r == m-1 and c == n-1:
                return 1
            
            if memo[r][c] != -1:
                return memo[r][c]
            
            memo[r][c] = dfs(r+1, c) + dfs(r, c+1)
            return memo[r][c]
        
        
        return dfs(0, 0)