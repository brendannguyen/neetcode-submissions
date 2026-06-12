class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        maxHeap = stones
        heapq.heapify_max(maxHeap) # or normal min heap and make invert all values (*-1)

        while maxHeap:
            if len(maxHeap) == 1:
                return maxHeap[0]
            
            res = heapq.heappop_max(maxHeap) - heapq.heappop_max(maxHeap)
            if res != 0:
                heapq.heappush_max(maxHeap, res)

        
        return 0
