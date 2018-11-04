class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        freq = {}
        for i in s:
            if i in freq.keys():
                freq[i] += 1
            else:
                freq[i] = 1
        # print freq

        j = freq.values().index(max(freq.values()))
        # print freq.keys()[j]
        letter = freq.keys()[j]
        index = s.index(freq.keys()[j])
        temp = index
        temps = [0] * len(s)
        print "ind", temp

        while k > 0 and temp < len(s):
            print k
            if s[temp ] != letter:
                temps[temp ] = letter
                k -= 1
            temp += 1

        while k > 0 and index > 0:

            if s[index] != letter:
                temps[index] = letter
                k -= 1
            index -= 1

        for i in range(len(temps)):
            if temps[i] == 0:
                temps[i] = s[i]
        temps = ''.join(temps)
        length = temps.index(letter)
        print temps
        ct = 0

        while length < len(temps) and temps[length] == letter:
            ct += 1
            length += 1
        return ct

a = Solution()
print a.characterReplacement("AABABBA",1)