#attribution - www.leetcode.com
# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict1 = {}
        s = list(s)
        for i in s :
            if i in dict1.keys():
                dict1[i] += 1
            else:
                dict1[i] = 1
        
        for i in s:
            if dict1[i] == 1:
                return s.index(i)
        
        return -1