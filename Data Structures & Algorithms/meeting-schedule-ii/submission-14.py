"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        if not intervals:
            return 0
        heap = []
        heapq.heappush(heap, intervals[0].end)

        for interval in intervals[1:]:
            if interval.start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, interval.end)

        return len(heap)


        