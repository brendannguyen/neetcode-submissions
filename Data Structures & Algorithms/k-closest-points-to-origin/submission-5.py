class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # minHeap based on eucli distance
        # input (dist, [x, y]) into heap
        # O(n + k log n)

        minHeap = []
        for point in points:
            eucli_d = (((point[0] - 0)**2) + ((point[1] - 0)**2)) ** 0.5
            heapq.heappush(minHeap, (eucli_d, point))
        
        result = []
        for i in range(k):
            result.append(heapq.heappop(minHeap)[1])

        return result
