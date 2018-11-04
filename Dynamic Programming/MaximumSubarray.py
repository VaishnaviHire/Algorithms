# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
# Example:
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:
#
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
#

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        opt = [0] * n
        opt[0] = nums[0]
        max_value = nums[0]
        for i in range(1,n):
            if opt[i-1] < 0:
                opt[i] = nums[i]
            else:
                opt[i] = nums[i] + opt[i-1]

            max_value = max(opt[i],max_value)

        return max_value




a = Solution()
print a.maxSubArray([-2,-1])
