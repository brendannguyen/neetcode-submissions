class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')]*n
        prices[src] = 0

        for i in range(k+1):
            pricesCopy = prices.copy() # so current iteration updates dont cascade to other edge price calcuations (normal bellman ford allows this as not doing k stops)
            for start, dest, price in flights:
                if prices[start] != float('inf') and pricesCopy[dest] > prices[start] + price:
                    pricesCopy[dest] = prices[start] + price
            prices = pricesCopy

        return -1 if prices[dst] == float('inf') else prices[dst]