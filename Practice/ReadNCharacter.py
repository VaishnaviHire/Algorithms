# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        if buf == "":
            return ""
        if n == 0:
            return ""
        if n < 4:
            return buf
        i = 0
        temp = ""
        while i < len(buf) or i < n:
            temp += read4(buf[i:])
            i += 4

