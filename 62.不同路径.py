#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#


# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # f(i, j) = f(i-1, j) + f(i, j-1)
        #
        # matrix = [[1 for _ in range(n)] for _ in range(m)]
        # for i in range(1, m):
        #     for j in range(1, n):
        #         matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        # return matrix[m-1][n-1]
        import math
        return int(
            math.factorial(m + n - 2) / math.factorial(m - 1) / math.factorial(n - 1)
        )


# @lc code=end
