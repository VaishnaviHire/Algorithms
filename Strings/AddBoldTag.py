class Solution:
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        res = []
        for i in dict:
            if i in s:
                res.append((s.index(i), s.index(i) + len(i) - 1))

        res = sorted(res)
        res_temp = [(res[0])]

        for n in res[1:]:
            if n[0] <= res_temp[-1][1]:
                res_temp[-1]= (min(res_temp[-1][0],n[0]),max(n[1], res_temp[-1][1]))
            else: res_temp.append(n)

        print(res_temp)




a = Solution()
a.addBoldTag("aaabbcc",["aaa","aab","bc"])