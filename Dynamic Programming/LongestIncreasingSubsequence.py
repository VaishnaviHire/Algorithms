# Given an unsorted array of integers, find the length of longest increasing subsequence.
#
# Example:
#
# Input: [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return 1

        opt = [1]*len(nums)
        # prev = float('-inf')

        opt[0] = 1
        for i in range(1,len(opt)):
            for j in range(0,i):
                if nums[i] > nums[j]:
                    opt[i] = max(opt[j]+1,opt[i])

        return max(opt)

a = Solution()
print a.lengthOfLIS([4,10,4,3,8,9])


