class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxElements = []
        l,r = 0,0
        queue = []
        prevMax = nums[0]

        while r < len(nums):
            while queue and l > queue[0]:
                queue.pop(0)
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r)    

            if (r-l+1) < k:
                r += 1
            else:
                maxElements.append(nums[queue[0]])
                l += 1
                r += 1
           
        return maxElements