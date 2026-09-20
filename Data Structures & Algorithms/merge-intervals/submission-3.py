class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        mergedIntervals = [intervals[0]]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            prevStart, prevEnd = mergedIntervals[-1]
            if start <= prevEnd:
                mergedIntervals[-1][1] = max(prevEnd, end)
            else:
                mergedIntervals.append(intervals[i])

        return mergedIntervals