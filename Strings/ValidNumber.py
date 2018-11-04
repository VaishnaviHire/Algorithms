import re
class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """

        p = re.compile('^[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?$') #For floats, integers,exponentials
        dot_case = len(s.strip().split('.'))
        ends_with_numbers = re.search(r'\d+$', s.strip())
        ends_with_dot = re.search(r'\d+\.$', s.strip())
        oper = re.search(r'^\d([-+*/]|([+-]?(?![eE])[a-zA-z]))', s.strip())

        if p.match(s.strip()) and len(s.strip().split(' ')) == 1 and dot_case <= 2:
            if ends_with_dot: # for cases like 3.
                return True
            elif not ends_with_numbers: #for cases like 50e
                return False
            elif oper: # for cases like 6+10, 8j7, 53F7
                return False
            return True
        return False

a = Solution()
print a.isNumber('6e6.5')