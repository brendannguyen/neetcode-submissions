class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # sort first
        intervals.sort(key=lambda pair: pair[0])

        result = []
        for interval in intervals:
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])

        return result