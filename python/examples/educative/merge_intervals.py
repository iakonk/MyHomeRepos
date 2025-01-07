"""
Given a list of intervals, merge all the overlapping intervals to produce
a list that has only mutually exclusive intervals.

Example 1:

Intervals: [[1,4], [2,5], [7,9]]
Output: [[1,5], [7,9]]
Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into
one [1,5].
"""


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print(self):
        print('[', self.start, ',', self.end, ']')


class Solution:
    def merge_intervals(self, intervals):
        if len(intervals) < 2:
            return intervals

        intervals.sort(key=lambda x: x.start)

        res = []
        start, end = intervals[0].start, intervals[0].end
        for interval in intervals:
            if interval.start <= end:
                end = max(interval.end, end)
            else:
                res.append(Interval(start, end))
                start, end = interval.start, interval.end
        res.append(Interval(start, end))
        return res


def main():
    print("Merged intervals: ", end='')
    for interval in Solution().merge_intervals([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        interval.print()


main()
