# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

class Solution(object):
    def twoSum(self,nums,target):
        track = {}
        for i in range(len(nums)):
            if nums[i] in track.keys():
                return [nums[i],-target, track[nums[i]]]
            else:
                track[target-nums[i]] = nums[i]


    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums= sorted(nums)
        for i in range(len(nums)):
            if i == 0:
                temp = nums[1:]
            else:
                temp = nums[:i] + nums[i+1:]
            if self.twoSum(temp,-nums[i]):
                result.append(sorted(self.twoSum(temp,-nums[i])))
        a = ((set(tuple(x) for x in result)))
        res = []
        for i in a:
            res.append(list(i))
        return res

a = Solution()
print a.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6])
