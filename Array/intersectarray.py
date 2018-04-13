# attribution: www.leetcode.com
# Given two arrays, write a function to compute their intersection.

# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        if nums1 == [] or nums2 == []:
            return []
        else:
            m = len(nums1)
            n = len(nums2)
            result = []
            if m <= n:
                for i in nums1:
                    if i in nums2:
                        result.append(i)
                        nums2.remove(i)

            else:
                for j in nums2:
                    if j in nums1:
                        result.append(j)
                        nums1.remove(j)
            
            return result