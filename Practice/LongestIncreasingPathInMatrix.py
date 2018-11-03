# Given an integer matrix, find the length of the longest increasing path.
#
# From each cell, you can either move to four directions: left, right, up or down.
# You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).
#
# Example 1:
#
# Input: nums =
# [
#   [9,9,4],
#   [6,6,8],
#   [2,1,1]
# ]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].
# Example 2:
#
# Input: nums =
# [
#   [3,4,5],
#   [3,2,6],
#   [2,2,1]
# ]
# Output: 4
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

class Solution(object):
    def dfs(self,matrix,x,y,prev, path):
        if x < 0 or y < 0 or x > len(matrix)-1 or y > len(matrix[0])-1:

            return 0
        curr = matrix[x][y]
        if curr > prev:
            if path.get((x,y)):
                return path[(x,y)]
            else:
                path[(x,y)] = 1 + max(self.dfs(matrix,x-1,y,curr,path),self.dfs(matrix,x+1,y,curr,path), self.dfs(matrix,x,y-1,curr,path), self.dfs(matrix,x,y+1,curr,path))
                return path[(x,y)]
        else:
            return 0



    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        if not matrix:
            return 0

        path = {}
        prev = float('-inf')
        r = float('-inf')
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                r = max(r, self.dfs(matrix,i,j,prev, path))
        return r

a = Solution()
print a.longestIncreasingPath([
  [3,4,5],
  [3,2,6],
  [2,2,1]
])
