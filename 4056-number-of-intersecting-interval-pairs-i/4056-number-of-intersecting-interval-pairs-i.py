class Solution(object):
    def countIntersectingIntervals(self, intervals):
        starts = sorted(x[0] for x in intervals)
        ends = sorted(x[1] for x in intervals)
        count = 0
        j = 0
        for i in range(len(intervals)):
            while j < len(intervals) and ends[j] < starts[i]:
                j += 1
            count += i - j
        return count