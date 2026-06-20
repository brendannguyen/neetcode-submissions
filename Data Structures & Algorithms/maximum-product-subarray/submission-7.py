class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        curMin, curMax = 1, 1 # neutral value

        for n in nums:
            temp = curMax
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(n * temp, n * curMin, n)

            result = max(result, curMax, curMin)

        return result

