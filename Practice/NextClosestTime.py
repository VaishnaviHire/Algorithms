class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        s = time.split(':')
        mini = 60 * int(s[0]) + int(s[1])
        l = [int(d) for d in s[0]]
        l += [int(d) for d in s[1]]
        l = list(set(l))
        a = 60 * 24
        while True:
            mini = (mini + 1) % (a)
            hr, mint = divmod(mini, 60)
            str_hr = str(hr)
            str_min = str(mint)

            if len(str_hr) == 1:
                str_hr = "0" + str_hr
            if len(str_min) == 1:
                str_min = "0" + str_min
            combined = []
            for i in (str_hr + str_min):
                combined.append(int(i))

            if all(i in l for i in list(set(combined))):
                return ":".join([str_hr, str_min])





a = Solution()
print a.nextClosestTime("23:58")