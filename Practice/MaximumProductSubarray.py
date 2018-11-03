# Given an integer array nums, find the contiguous subarray
# within an array (containing at least one number) which has the largest product.
#
# Example 1:
#
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:
#
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot

from operator import mul

class Solution(object):
    def maxProduct(self,nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        max_product =  reduce(mul, nums, 1)
        curr_product = reduce(mul, nums, 1)
        left = 0
        right = len(nums) - 1
        curr = 1

        while left <= right:
            # print curr_product,left, right
            if curr != 0:
                curr_product = (curr_product) / curr


            print curr_product
            if curr_product >= max_product:
                max_product = max(curr_product, curr)
                curr = nums[right]

                right -= 1
                print curr_product,curr


            else:
                max_product = max(max_product, curr)
                curr = nums[left]
                left += 1
                print "in else"
                print(max_product,curr)


        return max_product


a = Solution()
print a.maxProduct([2,3,-2,4])
