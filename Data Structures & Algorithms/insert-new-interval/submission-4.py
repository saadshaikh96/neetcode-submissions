class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        finalIntervals = []
        newIntervalStart, newIntervalEnd = newInterval
    
        i = 0
        while i < len(intervals) and intervals[i][1] < newIntervalStart:
            finalIntervals.append(intervals[i])
            i += 1

        while i < len(intervals) and newIntervalEnd >= intervals[i][0]:
            newIntervalStart = min(newIntervalStart, intervals[i][0])
            newIntervalEnd = max(newIntervalEnd, intervals[i][1])
            i += 1
        finalIntervals.append([newIntervalStart, newIntervalEnd])

        while i < len(intervals):
            finalIntervals.append(intervals[i])
            i += 1

        return finalIntervals
                