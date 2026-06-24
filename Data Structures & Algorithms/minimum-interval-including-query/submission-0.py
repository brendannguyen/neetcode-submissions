class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # sort
        intervals.sort(key=lambda pair: pair[0])

        result = {}
        minHeap = []
        i = 0

        for query in sorted(queries):
            # add to min heap until reach end or reach interval that is bigger than query time
            while i < len(intervals) and intervals[i][0] <= query:
                start, end = intervals[i]
                heapq.heappush(minHeap, (end - start + 1, end))
                i += 1
            
            # go through min heap until find period that contains query (get the smallest)
            while minHeap and minHeap[0][1] < query:
                heapq.heappop(minHeap)
            
            if minHeap:
                result[query] = minHeap[0][0]
            else:
                result[query] = -1
        
        return [result[q] for q in queries]