#attribution: www.leetcode.com
# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n ==2:
            return 2
        else:
        
            opt = [0] * (n + 1)
            opt[1] = 1
            opt[2] = 2


            for i in range(3, n + 1):
                opt[i] = opt[i-1] + opt[i - 2]


            return opt[n]