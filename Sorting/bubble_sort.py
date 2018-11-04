
class Solution:
    def bubble_sort(self,nums):
        for i in range(1, len(nums)):
            for j in range(1,len(nums)):
                if nums[j-1] > nums[j]:
                    temp = nums[j-1]
                    nums[j-1] = nums[j]
                    nums[j] = temp
        return nums

# larger numbers bubble up at the end
    def optimized_bubble_sort(self,nums):
        for i in range(1, len(nums)):
            for j in range(1,len(nums)-(i-1)):
                if nums[j-1] > nums[j]:
                    temp = nums[j-1]
                    nums[j-1] = nums[j]
                    nums[j] = temp

        return nums


a = Solution()
print a.bubble_sort([9, 7, 4, 1, 2,-1])
print a.optimized_bubble_sort([9, 7, 4, 1, 2,-1])
