# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
import itertools
class Solution(object):
    def isValid(self,pars):
        stack = []
        for bracket in pars:
            if bracket == '(':
                stack.append(bracket)
            elif not stack:
                return False
            elif bracket == ')':
                stack.pop()
        return not stack

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0 :
            return []

        if n == 1:
            return ['()']

        par = ['(']*(n-1) + [')']*(n-1)
        ab = set(itertools.permutations(par,len(par)))
        result = []
        temp = []

        for i in ab:
            i = ['('] + list(i) + [')']
            temp.append(i)

        for i in temp:
            if self.isValid(i):
                result.append(''.join(i))
        return result

# Backtracking Solution:

    # def generateParenthesis(self, n):
    #     """
    #     :type n: int
    #     :rtype: List[str]
    #     """
    #     result, path = [], ''
    #     self.backtrack(n,0,0,result,path)
    #     return result
    #
    # def backtrack(self, n, num_open, num_closed, result, path):
    #     if num_closed == n:
    #         result.append(path)
    #         return
    #     else:
    #         if num_open < n:
    #             path += '('
    #             num_open += 1
    #             self.backtrack(n,num_open,num_closed,result,path)
    #             path = path[:-1]
    #             num_open -= 1
    #
    #         if num_open > num_closed:
    #             path += ')'
    #             num_closed +=1
    #             self.backtrack(n,num_open,num_closed,result,path)
    #             path = path[:-1]
    #             num_closed -= 1
    #     return

a = Solution()
print a.generateParenthesis(6)
