class Solution:
    def rob(self, nums: List[int]) -> int:
        # either rob first house or rob second house, cannot be both
        # house robber I approach but for nums[:-1] and for nums[1:]
        # max of those two is the answer
        
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        def _rob(nums: List[int]) -> int:
            
            if not nums:
                return 0
            if len(nums) == 1:
                return nums[0]

            dp = [0 for i in range(len(nums))]
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])

            return dp[-1]

        return max(_rob(nums[:-1]), _rob(nums[1:]))
            