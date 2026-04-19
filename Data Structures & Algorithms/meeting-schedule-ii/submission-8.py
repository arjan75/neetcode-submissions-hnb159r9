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
        if intervals == []:
            return 0
        
        intervals.sort(key=lambda x:x.start)
        ongoingMeetings = []
        ongoingMeetings.append(intervals[0].end)

        for i in range(1, len(intervals)):
            if intervals[i].start >= ongoingMeetings[0]:
                heapq.heappop(ongoingMeetings)
            heapq.heappush(ongoingMeetings, intervals[i].end)
        return len(ongoingMeetings)
        
            

        

        