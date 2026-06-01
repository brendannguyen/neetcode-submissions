class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxElements = []
        l,r = 0,0
        queue = []
        head = 0

        while r < len(nums):
            while len(queue) > head and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r)

            if len(queue) > head and queue[head] < l:
                head += 1

            if (r-l+1) < k:
                r += 1
            else:
                maxElements.append(nums[queue[head]])
                l += 1
                r += 1
           
        return maxElements