class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # instead of choosing the first balloon to burst, choose the last balloon to burst in a subarray.
        nums = [1] + nums + [1]
        memo = {}

        def dfs(l, r):
            if l > r:
                return 0 # no balloons to burst
            
            if (l, r) in memo:
                return memo[(l, r)]

            memo[(l, r)] = 0
            for i in range(l, r+1):
                # burst balloon
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                # best coins from left side + right side
                coins += dfs(l, i-1) + dfs(i+1, r)
                # set to max of iteration
                memo[(l, r)] = max(memo[(l, r)], coins)
            
            return memo[(l, r)]

        # left most and right most index (not including placed 1s)
        return dfs(1, len(nums)-2)