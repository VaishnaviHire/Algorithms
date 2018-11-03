# A selection sort algorithm sorts through a list of items by iterating through a list of elements, finding the smallest one, and putting it aside into a sorted list.
# It continues to sort by finding the smallest unsorted element, and adding it to the sorted list.

# A selection sort algorithm will divide its input list into a sorted and an unsorted section.

class Solution:
    def selection_sort(self,nums):

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j]<nums[i]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp

        return nums

a = Solution()
print a.selection_sort([1,5,2,8,4,0,4,-1])
