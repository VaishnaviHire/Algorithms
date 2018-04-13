#attribution: www.leetcode.com
# Rotate an array of n elements to the right by k steps.

# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
            
        if (nums != [] and len(nums) != 1 and len(nums) != 2) and len(nums) >= k:
            l = list(nums[n-k:])
            r = list(nums[:n-k])
            nums[:] = l+r
         
        
        if len(nums) == 2 and k == 1 and len(nums) >= k:
            l = list([nums[1]])
            r = list([nums[0]])
            print( l + r)
            nums[:] = l + r
            