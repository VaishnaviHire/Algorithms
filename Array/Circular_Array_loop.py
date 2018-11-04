class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        for i in range(len(nums)):
            start = i
            path = []
            while start not in path:
                if nums[i] < 0:
                    i -= abs(nums[i])
                    # path.append(i)
                    if i < 0:
                        i = len(nums) + i
                        path.append(i)
                    else:
                        path.append(i)

                if nums[i] >= 0:
                    i += nums[i]
                    if i > len(nums) - 1:
                        i = i - len(nums)
                        path.append(i)
                    else:
                        path.append(i)
                print path

                if len(path) > len(nums):
                    return False

            return True

a = Solution()
print a.circularArrayLoop([2, -1, 1, 2, 2])