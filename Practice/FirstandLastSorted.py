# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].

# Example 1:
#
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
#
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

class Solution(object):
    def binary_search(self,nums, key):
        if nums:
            n = len(nums)
            mid = int(n/2)
            start = 0
            end = n-1

            while start < end:
                print start,mid, end
                if nums[mid] == key:
                    return mid
                if nums[mid] > key:
                    end = mid
                    mid = int((start + end) / 2)
                if nums[mid]<key:
                    print("here")
                    start = mid + 1

                    mid = int((start + end) / 2)
                    print mid
            if nums[-1] == key:
                return n-1
        return -1

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 1 and nums[0]==target:
            return [0,0]
        index = self.binary_search(nums,target)
        if index == -1:
            return [-1, -1]

        i = index
        j = index

        while i < len(nums) and nums[i] == target:
            i +=1
        print i

        while j > -1 and nums[j] == target:
            j -= 1


        return  [j+1,i-1]

a = Solution()
print a.searchRange([5,7,7,8,8,10],6)