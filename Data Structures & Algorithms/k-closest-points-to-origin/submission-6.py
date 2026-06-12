class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # maxHeap based on eucli distance
        # input (dist, [x, y]) into heap
        # if len(maxHeap) > k, pop highest value (furthest point away)
        # O(nlogk)

        maxHeap = []
        for point in points:
            eucli_d = (((point[0] - 0)**2) + ((point[1] - 0)**2)) ** 0.5
            heapq.heappush_max(maxHeap, (eucli_d, point))
            if len(maxHeap) > k:
                heapq.heappop_max(maxHeap)
            
        
        result = []
        while maxHeap:
            result.append(heapq.heappop_max(maxHeap)[1])

        return result
