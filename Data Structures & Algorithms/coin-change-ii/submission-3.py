class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
  
        memo = {}

        def dfs(amount, i):
            if amount == 0:
                return 1
            if i >= len(coins):
                return 0
            if (amount, i) in memo:
                return memo[(amount, i)]
            
            result = dfs(amount, i+1)

            if amount >= coins[i]:
                result += dfs(amount-coins[i], i)
            
            memo[(amount, i)] = result
            return result
        
        return dfs(amount, 0)