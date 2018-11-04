class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if target not in nums:
            return -1

        n = len(nums)
        mid = int(n /2)
        low = 0
        high = n
        while low  < high:
            # print mid
            if target > nums[mid]:
                low = mid
            elif nums[mid] > target:
                high = mid
            else:
                return mid
            mid = int ((low+high) / 2)

        return mid

a = Solution()
print a.search([-1,0,3,5,9,12],9)