class Solution:
    def jump(self, nums: List[int]) -> int:
        # greedy approach, bfs type of solution, look through each section that can be reached
        # no. of sections = minimum steps
        result = 0
        l, r = 0, 0

        while r < len(nums) - 1:
            furthest = 0
            for i in range(l, r+1):
                furthest = max(furthest, i + nums[i])
            l = r+1
            r = furthest
            result += 1
        
        return result