# According to the Wikipedia's article: "The Game of Life, also known simply as Life,
# is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
#
# Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts
# with its eight neighbors (horizontal, vertical, diagonal) using the following four rules
#  (taken from the above Wikipedia article):
#
# Any live cell with fewer than two live neighbors dies, as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# Write a function to compute the next state (after one update) of the board given its current state.
# The next state is created by applying the above rules simultaneously to every cell in the current state,
# where births and deaths occur simultaneously.
#
# Example:
#
# Input:
# [
#   [0,1,0],
#   [0,0,1],
#   [1,1,1],
#   [0,0,0]
# ]
# Output:
# [
#   [0,0,0],
#   [1,0,1],
#   [0,1,1],
#   [0,1,0]
# ]
# Follow up:
#
# Could you solve it in-place? Remember that the board needs to be updated at the same time:
# You cannot update some cells first and then use their updated values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the board is infinite,
# which would cause problems when the active area encroaches the border of the array.
# How would you address these problems?

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        result = [[0]*len(board[0])]*len(board)



        for x in range(len(board)):
            for y in range(len(board[0])):
                live_neighs = 0
                if board[x+1][y]:
                    live_neighs +=1
                if x-1 and board[x-1][y]:
                    live_neighs += 1
                if y-1 and board[x][y-1]:
                    live_neighs +=1
                if board[x][y+1] :
                    live_neighs +=1
                if x-1 and y-1 and board[x-1][y-1]:
                    live_neighs +=1
                if x-1 and y+1 and board[x-1][y+1]:
                    live_neighs +=1
                if x+1 and y-1 and board[x+1][y-1]:
                    live_neighs +=1
                if x+1 and y+1 and board[x+1][y+1]:
                    live_neighs +=1

                if board[x][y]:
                    if live_neighs < 2 or live_neighs > 3:
                        result[x][y] = 0
                elif live_neighs == 3:
                    result[x][y] = 1
                else:
                    result[x][y] = 0

        return result


a = Solution()
print a.gameOfLife([
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
])



