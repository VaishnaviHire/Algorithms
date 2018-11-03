#
# Example 1:
#
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:
#
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        intervals = sorted(intervals,key= lambda k : [k.start,k.end])

        for i in intervals:
            print i.start, i.end

        result = [intervals[0]]
        for i in range(1,len(intervals)):
            if result[-1].end >= intervals[i].start:
                print "dghj"
                mer = result.pop()
                mer.end = max(intervals[i].end,mer.end)
                result.append(mer)

            else:
                result.append(intervals[i])

        for i in result:
            print i.start, i.end

        return result




a1 = Interval(0,4)
a2 =Interval(1,4)
a3 = Interval(8,10)
a4 = Interval(15,18)
a = Solution()
a.merge([a1,a2,a3,a4])