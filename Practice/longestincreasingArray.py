class Solution(object):
    def dfs(self, matrix, x, y, prev, path):

        if x < 0 or x > len(matrix) - 1 or y < 0 or y > len(matrix[0]) - 1:
            return 0
        cur = matrix[x][y]

        if cur > prev:
            if path.get((x, y)):
                return path.get((x, y))
            else:
                r = 1 + max(self.dfs(matrix, x - 1, y, cur, path), self.dfs(matrix, x + 1, y, cur, path),
                            self.dfs(matrix, x, y - 1, cur, path), self.dfs(matrix, x, y + 1, cur, path))
                path[(x, y)] = r
                return r
        else:
            return 0

    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        result = []
        if not matrix or not matrix[0]:
            return 0
        # if len(matrix) == 1:
        #     return 1
        path = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result.append(self.dfs(matrix, i, j, float('-inf'), path))

        return max(result)

a= Solution()
print a.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]])