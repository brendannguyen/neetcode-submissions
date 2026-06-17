class Solution:
    def climbStairs(self, n: int) -> int:
        # dp bottom up, solve smallest subproblems first, then work way up
        # to reach step i, you only come from:
            # step i-1
            # step i-2

        if n <= 2:
            return n

        dp = [0 for i in range(n+1)]
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]