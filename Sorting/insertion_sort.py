class Solution:

    def insertion_sort(self,nums):
        sorted = [nums[0]]
        for i in range(1, len(nums)):
            for j in range(len(sorted)):
                if nums[i]< sorted[j]:
                    sorted.insert(j,nums[i])
                    break
            if nums[i] not in sorted:
                sorted.append(nums[i])

        return sorted

# Try doing this in-place
a = Solution()
print a.insertion_sort([2,6,1,4,5,8,9,0])
