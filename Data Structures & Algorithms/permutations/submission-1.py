class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # O(n * n!)
        result = []
        used = [False] * len(nums)

        def dfs(current_combo):

            if len(current_combo) == len(nums):
                result.append(current_combo.copy())
                return
            
            # add rest
            for i in range(len(nums)):
                if used[i]:
                    continue
                
                used[i] = True
                current_combo.append(nums[i])
                dfs(current_combo)

                current_combo.pop()
                used[i] = False

        dfs([])
        return result