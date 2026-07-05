class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        newList = []
        if len(intervals) <= 1:
            return intervals
        
        intervals.sort(key=lambda x:x[0])
        newList.append(intervals[0])

        for i in range(1, len(intervals)):
            if intervals[i][0] <= newList[-1][1]:
                value = newList.pop()
                newList.append([min(value[0], intervals[i][0]), max(value[1], intervals[i][1])])
            else:
                newList.append(intervals[i])
        return newList
        