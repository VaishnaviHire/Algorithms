# Given an array of strings, group anagrams together.
#
# Example:
#
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:
#
# All inputs will be in lowercase.
# The order of your output does not matter.
from collections import defaultdict
class Solution(object):
    def groupAnagrams(self,arr):
        word_map = defaultdict(list)
        for i in arr:
            a1 = ''.join(sorted(list(i)))
            if a1 in word_map:
                word_map[a1].append(i)
            else:
                word_map[a1] = [i]
        result = []
        for key, value in word_map.iteritems():
            result.append(word_map[key])
        return result

a = Solution()
print a.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])