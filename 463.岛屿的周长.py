#
# @lc app=leetcode.cn id=463 lang=python3
#
# [463] 岛屿的周长
#


# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        row, col = len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                # if grid[i][j] == 0:
                #     continue
                # if (i - 1 >= 0 and grid[i - 1][j] == 0) or (i - 1 < 0):
                #     res += 1
                # if (i + 1 < row and grid[i + 1][j] == 0) or (i + 1 >= row):
                #     res += 1
                # if (j - 1 >= 0 and grid[i][j - 1] == 0) or (j - 1 < 0):
                #     res += 1
                # if (j + 1 < col and grid[i][j + 1] == 0) or (j + 1 >= col):
                #     res += 1
                if grid[i][j] == 1:
                    down = 2 if i + 1 < row and grid[i + 1][j] == 1 else 0
                    right = 2 if j + 1 < col and grid[i][j+1] == 1 else 0
                    res += 4 - down - right
        return res


# @lc code=end
