# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
#
# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.

# The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
import math

class Solution:
    def isPalindrome(self,s,l,r):
        while l<r:
            if(s[l] != s[r]):
                return False

            l +=1
            r -=1

        return True



    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s:
            l = 0
            r = len(s)-1
            if self.isPalindrome(s,l,r):
                return True
            else:

                while l < r:
                    if s[l] != s[r]:
                        return self.isPalindrome(s,l+1,r) or self.isPalindrome(s,l,r-1)
                return True
        return False






a = Solution()
print a.validPalindrome("abc")

# def validPalindrome(self, s):
#     """
#     :type s: str
#     :rtype: bool
#     """
#     i = 0
#     j = len(s) - 1
#     while i < j:
#         if s[i] != s[j]:
#             return self.isPalindrome(s, i+1, j) or self.isPalindrome(s, i, j-1)
#         i += 1
#         j -= 1
#     return True
#
# def isPalindrome(self, s, l, r):
#     while l < r:
#         if s[l] != s[r]:
#             return False
#         l += 1
#         r -= 1
#     return True


# def validPalindrome(self, s):
#     """
#     :type s: str
#     :rtype: bool
#     """
#     n = len(s)
#     if n == 0 or n == 1 or n == 2:
#         return True
#     else:
#         l = 0
#         r = n - 1
#         while l < r and s[l] == s[r]:
#             l += 1
#             r -= 1
#         if l >= r:
#             return True
#         else:
#             t = s[l + 1:r + 1]
#             t_prime = s[l:r]
#             return t == t[::-1] or t_prime == t_prime[::-1]
#         return False