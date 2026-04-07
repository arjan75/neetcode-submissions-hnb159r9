class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals == []:
            return intervals
        
        intervals.sort(key=lambda x: x[0])
        newIntervals = [intervals[0]]

        for i in range(1, len(intervals)):
            lastInterval = newIntervals.pop()
            if lastInterval[1] >= intervals[i][0]:
                newInterval = [lastInterval[0], max(lastInterval[1], intervals[i][1])]
                newIntervals.append(newInterval)
            else:
                newIntervals.append(lastInterval)
                newIntervals.append(intervals[i])
        return newIntervals

        