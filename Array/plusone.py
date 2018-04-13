# attribution: www.leetcode.com
# Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        n= len(digits)
        if n == 1 and digits[0] <= 8:
            return [digits[0] + 1]
        if n == 1 and digits[0] == 9:
            return [1,0]
        else:
            a = (len(digits)-1) * [0]
            a.append(1)
            result = []
            carry = 0
            for i in range(n):
                m = a[n-1-i] + digits[n-1-i] + carry
            

                if divmod(m,10)[0] != 0:
                    result.insert(0, divmod(m,10)[1])
                    carry = divmod(m,10)[0]
                else:
                    result.insert(0, m)
                    carry = 0
                    
            if carry != 0:
                result.insert(0,carry)

            return result

    
    
    