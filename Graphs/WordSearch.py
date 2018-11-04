# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells
# are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
# Example:
#
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.

class Solution(object):
    def search(self,board,x,y,word, curr_ind):
        if x >= 0 and x < len(board) and y >= 0 and y < len(board[0]) and board[x][y] == word[curr_ind]:
            print board
            if board[x][y] != word[0]:
                board[x][y] = '*'
            if curr_ind == len(word)-1:
                return True
            curr_ind +=1
            return self.search(board,x+1,y,word,curr_ind) or self.search(board,x-1,y,word,curr_ind) or self.search(board,x,y+1,word,curr_ind) or self.search(board,x,y-1,word,curr_ind)
        return False
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    temp = self.search(board,i,j,word,0)
                    if temp:
                        return temp

        return False

a = Solution()
print a.exist(
[["C","A","A"],["A","A","A"],["B","C","D"]],
"AAB")
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]