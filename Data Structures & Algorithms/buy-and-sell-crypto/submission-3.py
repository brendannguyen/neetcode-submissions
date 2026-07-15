class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        result = 0
        for i in range(1, len(prices)):
            result = max(result, prices[i] - minBuy)
            minBuy = min(minBuy, prices[i])
        
        return result