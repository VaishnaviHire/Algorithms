
#
# Input:  [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Input:  [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res =[]
        i = 0
        while i < len(nums):
            start = nums[i]
            print i
            if i < len(nums)-1:
                print "here"
                while i< len(nums)-1 :
                    if nums[i+1] - nums[i] == 1:
                        i += 1

                end = nums[i-1]
            else:
                end = nums[len(nums)-1]

            if start==end:
                res.append(str(start))
            else:
                res.append(str(start)+"->"+str(end))
            i +=1


        return res

a = Solution()
print a.summaryRanges([0,2,3,4,6,8,9])