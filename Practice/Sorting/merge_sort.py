
class Solution:
    def mergesort(self, nums):
        if len(nums) == 1:
            return nums

        mid = int(len(nums) / 2)

        left_arr = nums[:mid]
        right_arr = nums[mid:]

        self.mergesort(left_arr)
        self.mergesort(right_arr)
        self.merge(left_arr,right_arr,nums)

        return nums


    def merge(self, left_arr,right_arr, arr):
        left_len = len(left_arr)
        right_len = len(right_arr)


        i = 0
        j = 0
        k = 0
        while j < right_len and k < left_len:

            if left_arr[k] > right_arr[j]:
                arr[i] = right_arr[j]
                j +=1
            else:
                arr[i] = left_arr[k]
                k +=1
            i +=1

        while k < left_len:
            arr[i] = left_arr[k]
            i +=1
            k += 1

        while j < right_len:
            arr[i] = right_arr[j]
            i +=1
            j +=1








a = Solution()
print a.mergesort([1,5,2,8,4,0,4,-1,9])