class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadane's algorithm
        maxSum = nums[0]
        cur = 0
        
        for n in nums:
            if cur < 0:
                cur = 0
            cur += n
            maxSum = max(maxSum, cur)

        return maxSum
