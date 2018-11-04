class Solution(object):

    def isValid(self, s, index, left_count, right_count, invalid_left, invalid_right, curr_string):
        if index == len(s):
            if invalid_left == 0 and invalid_right == 0:
                self.result.add(curr_string)
        else:
            if s[index] == '(' and invalid_left > 0:
                self.isValid(s, index + 1, left_count, right_count, invalid_left - 1, invalid_right, curr_string)
            if s[index] == ')' and invalid_right > 0:
                self.isValid(s, index + 1, left_count, right_count, invalid_left, invalid_right - 1, curr_string)
            if s[index] != ')' and s[index] != '(':
                self.isValid(s, index + 1, left_count, right_count, invalid_left, invalid_right, curr_string + s[index])
            if s[index] == '(':
                self.isValid(s, index + 1, left_count + 1, right_count, invalid_left, invalid_right, curr_string+F)
            if s[index] == ')' and right_count < left_count:
                self.isValid(s, index + 1, left_count + 1, right_count, invalid_left, invalid_right, curr_string+')')

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.result = set()
        left = right = 0
        for i in s:
            if i == '(':
                left += 1
            elif i == ')' and left:
                left -= 1
            elif i == ')':
                right += 1

        self.isValid(s, 0, 0, 0, left, right, "")
        print self.result