class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # sort arrays
        # two pointers
        # if l + r > target, r - 1
        # if l + r < target, l + 1
        # if l = r

        nums_map = []
        for i, num in enumerate(nums):
            nums_map.append([num, i])

        nums_map.sort()
        l = 0
        r = len(nums) - 1

        while l < r:
            cur = nums_map[l][0] + nums_map[r][0]
            if cur == target:
                return [min(nums_map[l][1], nums_map[r][1]), max(nums_map[l][1], nums_map[r][1])]
            elif cur < target:
                l += 1
            else:
                r -= 1
        return False