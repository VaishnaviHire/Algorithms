# attribution: www.leetcode.com
# Given an array nums, write a function to move all 0's to the end of it
#  while maintaining the relative order of the non-zero elements.

# For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        c = 0
        
        if 0 in nums:
            for i in range(len(nums)):
             #   print(nums)
             #   print(i)
                if nums[i] == 0:
                    j = i
                    while nums[j] == 0 and j < len(nums) - 1:
                        j += 1
                    nums[j], nums[i] = nums[i], nums[j]