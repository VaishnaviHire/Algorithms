# Given a set of distinct integers, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
import itertools

#
# class Solution(object):
#     def subsets(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#
#         result = []
#         a1 = (itertools.chain(*map(lambda x : itertools.combinations(nums, x), range(0,len(nums) + 1))))
#         for subset in a1:
#             result.append(list(subset))
#         return result

#
class Solution(object):
    def subsets(self, nums):
        nums.sort()
        result = [[]]
        for num in nums:
            result += [i + [num] for i in result]
            print result
        return result

a = Solution()
print a.subsets([1,2,3])
