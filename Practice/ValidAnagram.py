# Given two strings s and t , write a function to determine if t is an anagram of s.
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false
# Note:
# You may assume the string contains only lowercase alphabets.
#
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?
class Solution(object):
    def valid_Anagrams(self,s,t):
        included = [0]* 256

        for i in s:
            if included[ord(i)]:
                included[ord(i)] += 1
            else:
                included[ord(i)] = 1

        for i in t:
            if not included[ord(i)]:
                return False
            else:
                included[ord(i)] -= 1
        return True

a = Solution()