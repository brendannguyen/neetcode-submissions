class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        n = len(intervals)
        target = newInterval[0]
        left, right = 0, n-1
        # binary search to insert new interval
        while left <= right:
            mid = (left+right) // 2
            if intervals[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        intervals.insert(left, newInterval)
        
        # merge intervals
        result = []
        for interval in intervals:
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
        
        return result