# attribution: www.leetcode.com
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        diff = {}
        for i in range(len(nums)):
            if nums[i] in diff:
                return [diff[nums[i]],i]
            else:
                diff[target - nums[i]]=i