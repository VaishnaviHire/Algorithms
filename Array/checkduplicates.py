#attribution: www.leetcode.com
# Given an array of integers, find if the array contains any duplicates. Your function should return true if any value 
# appears at least twice in the array, and it should return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict1 = {}
        for i in nums:
            if i in dict1.keys():
                return True
            else:
                dict1[i] = 1
        
        return False