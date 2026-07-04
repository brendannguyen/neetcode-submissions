class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # buy, sell, nothing

        # memo[i] = maxProfit you can get at this point

        memo = {}

        def dfs(i, bought):
            if i >= len(prices):
                return 0
            
            if (i, bought) in memo:
                return memo[(i, bought)]
            
            nothing = dfs(i+1, bought)
            if bought:
                memo[(i, bought)] = max(nothing, dfs(i+2, False) + prices[i])
            else:
                memo[(i, bought)] = max(nothing, dfs(i+1, True) - prices[i])

            return memo[(i, bought)]

        return dfs(0, False)
        

