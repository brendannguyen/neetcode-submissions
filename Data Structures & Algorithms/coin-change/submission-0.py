class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0

        seen = [False] * (amount + 1)
        seen[0] = True
        queue = deque([0])
        minCoins = 0

        while queue:
            minCoins += 1
            for i in range(len(queue)):
                curSum = queue.popleft()
                for coin in coins:
                    nextSum = curSum + coin
                    if nextSum == amount:
                        return minCoins
                    if nextSum > amount or seen[nextSum]:
                        continue
                    seen[nextSum] = True
                    queue.append(nextSum)

        
        return -1     