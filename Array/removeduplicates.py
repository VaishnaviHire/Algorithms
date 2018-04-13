#attribution: www.leetcode.com
# Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == [] :
            return 0
        else:
            l = 1
            s = 0
            for e in range(1,len(nums)):
                if nums[e] != nums[s]:
                    nums[s+1] = nums[e]
                    l += 1
                    s += 1
                    
            return l
                
