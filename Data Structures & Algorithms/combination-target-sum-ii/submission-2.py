class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        # so duplicates are next to each other
        candidates.sort()

        def dfs(i, current_combo, current_sum):

            # check sum meets target first (as previous candidate is added at end of function)
            if current_sum == target:
                result.append(current_combo.copy())
                return

            if i >= len(candidates) or current_sum > target:
                return

            
            # add next nums[i]
            current_combo.append(candidates[i])
            dfs(i+1, current_combo, current_sum + candidates[i])

            current_combo.pop()
            # skip until not at a duplicate
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1

            dfs(i+1, current_combo, current_sum)

        dfs(0, [], 0)

        return result