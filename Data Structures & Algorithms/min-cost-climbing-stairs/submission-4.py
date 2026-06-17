class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # top down

        memo = [-1 for i in range(len(cost)+1)]

        def dfs(n):
            if n == 0:
                memo[n] = 0
                return 0
            if n == 1:
                memo[n] = 0
                return 0
            
            if memo[n] != -1:
                return memo[n]

            memo[n] = min(dfs(n-1) + cost[n-1], dfs(n-2) + cost[n-2])
            return memo[n]

        return dfs(len(cost))
