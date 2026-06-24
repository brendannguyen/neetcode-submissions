class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadane's algorithm
        maxSum = nums[0]
        cur = 0
        r = 0

        while r < len(nums):
            cur += nums[r]
            maxSum = max(maxSum, cur)

            if cur < 0:
                cur = 0
            
            r += 1

        return maxSum
