class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        def dfs(current_combo, remaining):

            if len(current_combo) == len(nums):
                result.append(current_combo.copy())
                return
            
            # add rest
            for i in range(len(remaining)):
                dfs(current_combo + [remaining[i]], remaining[:i] + remaining[i+1:])

        dfs([], nums)
        return result