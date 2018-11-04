class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 1:
            return x
        elif n < 0:
            return (1.0) / self.myPow(x,-n)
        else:
            return x * self.myPow(x,n-1)


a = Solution()
print a.myPow(2.0,-6)