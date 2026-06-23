class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda pair: pair[1])
        
        end = float('-inf')
        result = 0
        for interval in intervals:
            if end <= interval[0]:
                end = interval[1]
            else:
                result += 1

        return result