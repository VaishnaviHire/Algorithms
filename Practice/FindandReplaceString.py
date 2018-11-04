class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        S = list(S)
        for i, x, y in sorted(zip(indexes, sources, targets), reverse = True):
            print i,x,y
            if all(i+k < len(S) and S[i+k] == x[k] for k in xrange(len(x))):
                S[i:i+len(x)] = list(y)
            print S

        return "".join(S)

a = Solution()
print a.findReplaceString("abbbddd",[0,2],["abbb","bbddd"],["eee","ffff"])


def countAndSay(self, n):
    """
    :type n: int
    :rtype: str
    """
    if n == 1:
        return '1'

    s = self.countAndSay(n - 1)  # make s the previous output

    # count how many numbers in s
    res = ''
    count = 1
    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            count += 1
        else:
            res += str(count) + s[i - 1]
            count = 1
    res += str(count) + s[-1::1]
    return res