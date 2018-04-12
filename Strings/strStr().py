#attribution - www.leetcode.com
# Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """     
        if needle == "" and haystack == "" or (needle == "" and haystack != ""):
            return 0
        if   (needle != "" and haystack == ""):
            return -1
        else:
            for i in range(len(haystack) - len(needle) + 1):
                #print(haystack[i:i+len(needle)] )
                if haystack[i:i+len(needle)] == needle:
                    return i
            return -1