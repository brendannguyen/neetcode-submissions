class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # top down

        memo = [-1 for i in range(len(cost))]

        def dfs(n):
            if n >= len(cost):
                return 0
            
            if memo[n] != -1:
                return memo[n]

            memo[n] = cost[n] + min(dfs(n+1), dfs(n+2))
            return memo[n]

        return min(dfs(0), dfs(1))
