class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxElements = []
        l,r = 0,0
        deq = collections.deque()
        prevMax = nums[0]
        head = 0

        while r < len(nums):
            while deq and nums[deq[-1]] < nums[r]:
                deq.pop()
            deq.append(r)    

            if deq[0] < l:
                deq.popleft()

            if (r-l+1) < k:
                r += 1
            else:
                maxElements.append(nums[deq[0]])
                l += 1
                r += 1
           
        return maxElements