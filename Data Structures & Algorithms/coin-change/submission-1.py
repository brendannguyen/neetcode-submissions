class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}

        def dfs(amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            
            result = float('inf')
            for coin in coins:
                if amount - coin >= 0:
                    result = min(result, 1 + dfs(amount - coin))
            
            memo[amount] = result
            return result
        
        result = dfs(amount)
        return result if result < float('inf') else -1