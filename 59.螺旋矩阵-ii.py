#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#
from typing import List


# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # matrix = [[0 for _ in range(n)] for _ in range(n)]
        # row, col = 0, 0
        # index = 1
        # row_f, col_f = 1, 1
        # while index <= n * n:

        #     while col < n and col > -1 and index <= n * n:
        #         matrix[row][col] = index
        #         index += 1
        #         if (
        #             col + col_f == n
        #             or col + col_f == -1
        #             or matrix[row][col + col_f] != 0
        #         ):
        #             col_f = -col_f
        #             row += row_f
        #             break
        #         col += col_f

        #     while row < n and row > -1 and index <= n * n:
        #         matrix[row][col] = index
        #         index += 1
        #         if (
        #             row + row_f == n
        #             or row + row_f == -1
        #             or matrix[row + row_f][col] != 0
        #         ):
        #             row_f = -row_f
        #             col += col_f
        #             break
        #         row += row_f

        # return matrix
        l, r, t, b = 0, n - 1, 0, n - 1
        mat = [[0 for _ in range(n)] for _ in range(n)]
        num, tar = 1, n * n
        while num <= tar:
            for i in range(l, r + 1): # left to right
                mat[t][i] = num
                num += 1
            t += 1
            for i in range(t, b + 1): # top to bottom
                mat[i][r] = num
                num += 1
            r -= 1
            for i in range(r, l - 1, -1): # right to left
                mat[b][i] = num
                num += 1
            b -= 1
            for i in range(b, t - 1, -1): # bottom to top
                mat[i][l] = num
                num += 1
            l += 1
        return mat

# @lc code=end
