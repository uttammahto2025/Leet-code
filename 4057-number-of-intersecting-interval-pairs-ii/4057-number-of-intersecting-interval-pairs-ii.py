class Solution(object):
    def countIntersectingIntervals(self, intervals):
        temoravlin = intervals

        starts = sorted(x[0] for x in temoravlin)
        ends = sorted(x[1] for x in temoravlin)

        n = len(intervals)
        count = 0
        j = 0

        for i in range(n):
            while j < n and ends[j] < starts[i]:
                j += 1

            count += i - j

        return count