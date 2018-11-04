class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        result = []
        temp = []

        for i in range(numRows):
            l = 0
            if i < (numRows - 1):
                # print(i)
                k = 2 * (numRows - i - 1)
                l = 2*i

                # print(temp)
            else:
                k = 2 * (numRows - 1)

            temp.append((k,l))
        print temp

        for i in range(len(temp)):
            j = i
            while j < len(s):
                result.append(s[j])
                j = j + temp[i][0]
                if j < len(s)-1 and temp[i][1]!=0:
                    result.append(s[j])
                    j = j + temp[i][1]

        return ''.join(result)



a = Solution()
print a.convert('PAYPALISHIRING',4)