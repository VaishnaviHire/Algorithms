# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
#
# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.

class Solution(object):
    def isValid(self,s,i,j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s)-1
        while i < j:
            print i,j
            if s[i] != s[j]:
                return  self.isValid(s,i+1,j) or self.isValid(s,i,j-1)
            i +=1
            j -=1

        return True



a = Solution()
a.validPalindrome("abdca")