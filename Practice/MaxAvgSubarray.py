class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        i = 0
        max_avg=[]
        while i+k < len(nums) + 1:
            sum1 = sum(nums[i:i+k])
            # print (sum1)
            max_avg_single = float(sum1) / float(k)
            for j in range(i+k, len(nums)):
                if max_avg_single  < (float(sum1+nums[j])/float(j+1)):
                    max_avg_single = float(sum1+nums[j])/float(j+1)
            max_avg.append(max_avg_single)
            i +=1
        print max_avg

a = Solution()
a.findMaxAverage([1,12,-5,-6,50,3],4)