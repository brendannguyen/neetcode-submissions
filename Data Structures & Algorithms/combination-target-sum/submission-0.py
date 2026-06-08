class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # add same number
        # add any of rest

        result = []

        def dfs(i, current_combo, current_sum):

            if i >= len(nums) or current_sum > target:
                return
            
            if current_sum == target:
                result.append(current_combo.copy())
                return
            
            # add same number
            current_combo.append(nums[i])
            dfs(i, current_combo, current_sum + nums[i])

            # add rest (must pop to backtrack to current state)
            current_combo.pop()
            dfs(i+1, current_combo, current_sum)

        dfs(0, [], 0)

        return result
