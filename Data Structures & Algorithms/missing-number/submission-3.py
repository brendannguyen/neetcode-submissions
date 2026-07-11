class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # XOR approach
        n = len(nums)
        result = n
        for i in range(n):
            result ^= i ^ nums[i]
        return result