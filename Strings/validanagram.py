#attribution - www.leetcode.com
# Given two strings s and t, write a function to determine if t is an anagram of s.

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        s = list(s)
        t = list(t)
        
        if len(s) != len(t):
            return False
        else:
            for i in s : 
                if i in t:
                    t.remove(i)
                    
            if t == []:
                return True
            else:
                return False
