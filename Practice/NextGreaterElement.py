class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0] * len(nums)
        for i in range(len(nums)):
            if i != len(nums) - 1:
                j = i + 1
            else:
                j = 0

            while nums[i] >= nums[j] :
                print i,j

                if j == i:
                    result[i] = -1
                    break
                elif j == len(nums) - 1:
                    j = 0
                else:
                    j += 1

            if result[i] != -1:
                    result[i] = nums[j]
        return result



a = Solution()
print a.nextGreaterElements([1,2,1])