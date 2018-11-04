class Solution(object):
    def subsets(self, nums):
        nums.sort()
        result = [[]]
        print result
        for num in nums:
            result += [i + [num] for i in result]
            print result

        return result

a = Solution()
a.subsets([1,2,3])