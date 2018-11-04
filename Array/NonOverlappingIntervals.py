# Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
#
# Note:
# You may assume the interval's end point is always bigger than its start point.
# Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
# Example 1:
# Input: [ [1,2], [2,3], [3,4], [1,3] ]
#
# Output: 1
#
# Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
# Example 2:
# Input: [ [1,2], [1,2], [1,2] ]
#
# Output: 2
#
# Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
# Example 3:
# Input: [ [1,2], [2,3] ]
#
# Output: 0
#
# Explanation: You don't need to

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals = sorted(intervals, key = lambda x : [x.start,x.end])
        stack = [intervals[0]]
        for i in intervals:
            print i.start, i.end

        for i in range(1,len(intervals)):
            stack_top = stack[-1]
            if (stack_top.end) <= (intervals[i].start):
                stack.append(intervals[i])

        return len(intervals) - len(stack)

# [[-100,-87],[-99,-44],[-98,-19],[-97,-33],[-96,-60],[-95,-17],[-94,-44],[-93,-9]]

a = Solution()
a1 = Interval(-100,-87)
a2 = Interval(-99,-44)
a3 = Interval(-98,-19)
a4 = Interval(-97,-33)
a5 = Interval(-96,-60)
a6 = Interval(-95,-17)
a7 = Interval(-94,-44)
a8 = Interval(93,99)
print a.eraseOverlapIntervals([a1,a2,a3,a4,a5,a6,a7,a8])

# public class Solution {
#     class myComparator implements Comparator<Interval> {
#         public int compare(Interval a, Interval b) {
#             return a.end - b.end;
#         }
#     }
#     public int eraseOverlapIntervals(Interval[] intervals) {
#         if (intervals.length == 0) {
#             return 0;
#         }
#         Arrays.sort(intervals, new myComparator());
#         int end = intervals[0].end;
#         int count = 1;
#         for (int i = 1; i < intervals.length; i++) {
#             if (intervals[i].start >= end) {
#                 end = intervals[i].end;
#                 count++;
#             }
#         }
#         return intervals.length - count;
#     }
# }