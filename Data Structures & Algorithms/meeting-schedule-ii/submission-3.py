"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda i: i.start)
        minHeap = [intervals[0].end]

        for i in range(1, len(intervals)):
            interval = intervals[i]
            if minHeap[0] <= interval.start:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, interval.end)
            else:
                heapq.heappush(minHeap, interval.end)

        return len(minHeap)