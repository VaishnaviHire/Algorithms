class Solution:
    def maxSubArray(self, nums) -> int:

        maxSum = nums[0]
        sum = [nums[0]]

        for i in range(1, len(nums)):
            sum.append(sum[i - 1] + nums[i])

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                sum_i_j = max(sum[j] - sum[i], sum[j])
                if (sum_i_j > maxSum):
                    maxSum = sum_i_j

        return maxSum


a = Solution()
print(a.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
