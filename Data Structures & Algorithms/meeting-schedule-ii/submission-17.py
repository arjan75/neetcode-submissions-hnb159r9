import heapq
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        endTimes = []
        if len(intervals) <= 1:
            return len(intervals)

        intervals.sort(key=lambda x: x.start)
        heapq.heappush(endTimes, intervals[0].end)

        for i in range(1, len(intervals)):
            startTime = intervals[i].start
            endTime = intervals[i].end

            if startTime >= endTimes[0]:
                heapq.heappop(endTimes)
            
            heapq.heappush(endTimes, endTime)
        return len(endTimes)



        