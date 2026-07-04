class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # buy, sell, nothing

        n = len(prices)
        dp = [[0, False] for i in range(n+1)]
        
        for i in range(n-1, -1, -1):
            for bought in [True, False]:
                nothing = dp[i+1][bought] if i+1 < n else 0
                if bought:
                    sell = (dp[i+2][False] + prices[i]) if i+2 < n else prices[i]
                    dp[i][bought] = max(nothing, sell)
                else:
                    buy = (dp[i+1][True] - prices[i]) if i+1 < n else (0 - prices[i])
                    dp[i][bought] = max(nothing, buy)


        return dp[0][False]
        

