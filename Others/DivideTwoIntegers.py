# Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
#
# Return the quotient after dividing dividend by divisor.
#
# The integer division should truncate toward zero.

# Example
# 1:
#
# Input: dividend = 10, divisor = 3
# Output: 3
# Example
# 2:
#
# Input: dividend = 7, divisor = -3
# Output: -2

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        quo = 0
        divisor_1 = abs(divisor)
        dividend_1 = abs(dividend)

        if divisor_1 == 1:
            quo = dividend_1
        else:
            while (dividend_1) >= (divisor_1):
                dividend_1 -= (divisor_1)
                quo += 1

        if (dividend < 0  and divisor > 0 ) or (dividend > 0  and divisor < 0):
            quo =  -quo

        if quo > (2 ** 31) - 1 :
            return (2 ** 31) -1
        if quo < -2 ** 31:
            return -2 ** 31


        return quo

a = Solution()
print a.divide(-2147483648,1)


