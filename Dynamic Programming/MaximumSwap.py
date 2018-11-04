# Given a non-negative integer, you could swap two digits at most once to get the maximum valued number.
# Return the maximum valued number you could get.
#
# Example 1:
# Input: 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
# Example 2:
# Input: 9973
# Output: 9973
# Explanation: No swap.
# Note:
# The given number is in the range [0, 108]

class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = map(int, str(num))
        dict1 = {}
        for i, x in enumerate(num):
            dict1[x] = i
        print dict1
        for i in range(len(num)):
            less = []
            for j in dict1.keys():
                if num[i] < j and i < dict1[j]:
                    less.append(j)
            if less:
                max_val = max(less)
                temp = num[i]
                num[i] = num[dict1[max_val]]
                num[dict1[max_val]] = temp
                break
        return int(''.join(map(str,num)))




a = Solution()
print a.maximumSwap(19931227)
