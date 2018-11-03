from pip._internal.commands.list import format_for_json


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.area = 0

        def dfs(grid,start_x,start_y):
            print start_x, start_y
            if start_x >= 0 and start_x < len(grid) and start_y>=0  and start_y< len(grid[0]) and  grid[start_x][start_y] == 1:
                self.area += grid[start_x][start_y]
                grid[start_x][start_y] = '*'
                dfs(grid,start_x+1,start_y)
                dfs(grid,start_x-1,start_y)
                dfs(grid,start_x,start_y+1)
                dfs(grid,start_x,start_y-1)

        result = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.area = 0
                    dfs(grid,i,j)
                    result.append(self.area)
        return max(result)


a1 = Solution()
print a1.maxAreaOfIsland([[0],[1]])