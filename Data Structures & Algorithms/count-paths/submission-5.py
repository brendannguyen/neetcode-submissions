class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # bottom up
        # dp[0][0] = 1
        # dp[m][n] = number of unique paths to get to that point
        # return dp[m-1][n-1]


        dp = [[0]*n for i in range(m)]
        dp[0][0] = 1
        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue
                paths = 0
                if r-1 >= 0:
                    paths += dp[r-1][c]
                if c-1 >= 0:
                    paths += dp[r][c-1]
                dp[r][c] = paths


        return dp[m-1][n-1]