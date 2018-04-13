# attribution: www.leetcode.com
# Given an array of integers, every element appears twice except for one. Find that single one
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums)==1:
            return nums[0]
        # print(nums)
        for i in range(0,len(nums)-1,2):
            print(nums[i])
          
            if nums[i]==nums[i+2] or nums[i]!=nums[i+1] :
                return nums[i]
            if nums[len(nums)-1]!= nums[len(nums)-2]:
                return nums[len(nums)-1]