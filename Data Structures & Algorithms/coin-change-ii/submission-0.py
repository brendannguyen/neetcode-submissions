class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
  
        memo = {}

        def dfs(amount, i):
            if amount == 0:
                return 1
            if (amount, i) in memo:
                return memo[(amount, i)]
            
            result = 0
            for j in range(i, len(coins)):
                if amount - coins[j] >= 0:
                    result += dfs(amount-coins[j], j)
            
            memo[(amount, i)] = result
            return result
        
        result = dfs(amount, 0)
        return result