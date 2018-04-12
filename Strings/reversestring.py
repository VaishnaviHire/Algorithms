#attribution - www.leetcode.com
# Write a function that takes a string as input and returns the string reversed.

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        j = len(s) - 1
        for i in range(len(s) // 2):
            s[i], s[j] = s[j], s[i]
            j -= 1
        
        return ''.join(s)