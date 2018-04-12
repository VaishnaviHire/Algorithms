#attribution - www.leetcode.com
# Given a 32-bit signed integer, reverse digits of an integer

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        a = ''
        m = abs(x)
        while divmod(m,10)[0]!=0:
            a = a + str(divmod(m,10)[1])
            m = divmod(m,10)[0]
        
        a= a + str(divmod(m,10)[1])
     
        if (int(a)>= 2 ** 31):
            return 0  
        else:
            return int(math.copysign(int(a),x))