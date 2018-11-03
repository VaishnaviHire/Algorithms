class Solution(object):
    # def validSubstring(self, s, k):
    #     visited = {}
    #     for i in s:
    #         if i not in visited.keys():
    #             visited[i] = 1
    #         else:
    #             visited[i] += 1
    #     return all(x >= k for x in visited.values())

    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        result = []
        sst = set(s)
        for i in sst:
            if s.count(i)<k:
                return max(self.longestSubstring(t,k) for t in s.split(i))

        return len(s)

        # for i in range(len(s)):
        #     for j in range(i,len(s)):
        #         print i,j
        #         if self.validSubstring(s[i:j+1],k):
        #             result.append((j-i) + 1)
        #
        # return  max(result)

a = Solution()
print a.longestSubstring('ababbalcdccddleeeffff',3)