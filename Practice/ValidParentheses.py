class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        brackets = {'(': ')', '{': '}', '[': ']'}

        stack = []
        if (s):
            for i in s:
                if (i in list(brackets.keys())):
                    stack.append(i)
                    print stack

                elif (stack != [] and i == brackets[str(stack[-1])]):
                    stack.pop()
                    print stack
                else:
                    return False

            if stack == []:
                return True
            else:
                return False
        else:
            return True


a=Solution()
print a.isValid('{{})')