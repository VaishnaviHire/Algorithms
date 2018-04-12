#attribution - www.leetcode.com
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """     
        if s == "":
            return True       
        else:
        
            for i in string.punctuation:
                s = s.replace(i,"")

            s = list(s.replace(" ","").lower())
        
            for i in range(len(s)):
              
                if s[i] != s[len(s) - 1 - i]:
                    return False
                               
            return True
