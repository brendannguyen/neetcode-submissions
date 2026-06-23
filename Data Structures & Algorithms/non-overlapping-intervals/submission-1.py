class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda pair: pair[1])
        
        newIntervals = []
        result = 0
        for interval in intervals:
            if not newIntervals or newIntervals[-1][1] <= interval[0]:
                newIntervals.append(interval)
            else:
                result += 1

        print(newIntervals)
        return result