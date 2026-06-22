class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # O(n^2)
        memo = {}

        def dfs(i, prevIdx):
            if (i, prevIdx) in memo:
                return memo[(i, prevIdx)]

            if i == len(nums):
                return 0

            result = dfs(i+1, prevIdx) # dont include i

            if prevIdx == -1 or nums[i] > nums[prevIdx]:
                result = max(result, dfs(i+1, i) + 1) # include i (dfs() + 1)

            memo[(i, prevIdx)] = result
            return result

        return dfs(0, -1)

