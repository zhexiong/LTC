# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        def compare(x, y):
            return x.start - y.start
        intervals = sorted(intervals, cmp=compare)
        # intervals = sorted(intervals, cmp=lambda x,y: x.start - y.start)
        # intervals = sorted(intervals, key=lambda x: x.start)
        result = []
        i = 0
        while i < len(intervals):
            interval = intervals[i]
            i += 1
            while i < len(intervals) and interval.end >= intervals[i].start:
                interval.end = max(interval.end, intervals[i].end)
                i += 1
            result.append(interval)
        return result