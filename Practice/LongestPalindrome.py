# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
#
# This is case sensitive, for example "Aa" is not considered a palindrome here.
#
# Note:
# Assume the length of given string will not exceed 1,010.
#
# Example:
#
# Input:
# "abccccdd"
#
# Output:
# 7
#
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
import numpy as np
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str

        """
        if s:
            l_pal = 1
        else:
            l_pal = 0
        if len(s) == 1:
            return 1
        if len(s) ==2 and s[0]==s[1]:
            return 2

        opt = np.array([[0] * (len(s))] * (len(s)))

        for i in range(len(opt)):
            opt[i][i] = True
            if i < len(opt[0]) -1 :
                opt[i][i+1] = (s[i] == s[i+1])
                if opt[i][i+1] and l_pal < len(s[i:i+2]):
                    l_pal = len(s[i:i+2])

        for i in range(2,len(opt)):
            for j in range(0,len(s)-i):
                k = i + j
                if s[k] == s[j] and opt[j+1][k-1]==1:
                    if l_pal < len(s[j:k+1]):
                        l_pal = len(s[j:k+1])
                    opt[j][k] = 1
        return l_pal

a = Solution()
print a.longestPalindrome("abccccdd")
