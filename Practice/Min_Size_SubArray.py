#
# Example:
#
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.
# Follow up:
# If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

class Solution:


    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left =0
        right = 0
        curr= 0
        diff = float('inf')
        n = len(nums)

        while left < n and right < n:
            while curr < s and right < n:
                curr += nums[right]
                print nums, curr,right
                right+=1

            print "***************************"

            while curr >= s and left < right:
                diff= min(diff, right-left)
                curr -= nums[left]
                print "overshot" ,nums,curr, left
                left+=1

        if diff == float('inf'):
            return 0
        else:
            return  diff






a = Solution()
print a.minSubArrayLen(213,[12,28,83,4,25,26,25,2,25,25,25,12])