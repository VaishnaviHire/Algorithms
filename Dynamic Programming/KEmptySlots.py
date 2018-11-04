from collections import OrderedDict
class Solution(object):
    def nearest_bloom(self,dict1,key):
        ahead = 0
        behind = 0
        for i in dict1.keys()[key:]:
            if dict1[i] == True:
                ahead = i
                break
        for i in dict1.keys()[:key-1]:
            if dict1[i] == True:
                behind = i
        # print key,ahead,behind

        if not ahead and not behind:
            return (-1,-1)
        # print("Ahead: ", ahead, "Behind: ", behind)
        if ahead and not behind:
            return (abs(key-ahead)-1,0)
        elif behind and not ahead:
            return (0,abs(key-behind)-1)


        return (abs(key - ahead)-1, abs(key-behind)-1)



    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        flower_map = OrderedDict()
        for i in range(1, len(flowers)+1):
            flower_map[i] = False
        for i in range(len(flowers)):

            flower_map[flowers[i]] = True
            # print i, flower_map
            # print self.nearest_bloom(flower_map,flowers[i])
            a = self.nearest_bloom(flower_map,flowers[i])
            if  a[0]== k or a[1] == k:
                # print "here"
                return i+1

        return -1



a = Solution()
print a.kEmptySlots([3,9,2,8,1,6,10,5,4,7]
,1)
