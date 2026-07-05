class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = {}

        # add 
        # subtract
        # if == target: return 1
        # if i >= nums: return 0
        # (i, amount)


        def dfs(i, currentSum):
            if currentSum == target and i == len(nums):
                return 1
            if i >= len(nums):
                return 0
            
            if (i, currentSum) in memo:
                return memo[(i, currentSum)]

            # add
            memo[(i, currentSum)] = dfs(i+1, currentSum - nums[i]) + dfs(i+1, currentSum + nums[i])

            return memo[(i, currentSum)]

        
        return dfs(0, 0)
            