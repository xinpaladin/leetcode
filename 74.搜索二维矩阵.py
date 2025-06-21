#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#


# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # rows = len(matrix)
        # cols = len(matrix[0])
        # for i in range(rows):
        #     if matrix[i][0] > target:
        #         return False
        #     if matrix[i][-1] < target:
        #         continue
        #     l, r = 0, cols
        #     while l < r:
        #         mid = (l + r) // 2
        #         if matrix[i][mid] == target:
        #             return True
        #         elif matrix[i][mid] > target:
        #             r = mid
        #         else:
        #             l = mid + 1
        #     return False
        # return False

        m, n = len(matrix), len(matrix[0])
        left, right = -1, m * n
        while left + 1 < right:
            mid = (left + right) // 2
            row, col = mid // n, mid % n
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                right = mid
            else:
                left = mid
        return False


# @lc code=end
