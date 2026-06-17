class Solution:
    def climbStairs(self, n: int) -> int:

        memo = [0 for i in range(n)]
        
        def dfs(n):
            
            if memo[n-1] != 0:
                return memo[n-1]

            if n == 1:
                memo[n-1] = 1
                return 1
            if n == 2:
                memo[n-1] = 2
                return 2
            
            memo[n-1] = dfs(n-1) + dfs(n-2)
            return memo[n-1]

    
        return dfs(n)