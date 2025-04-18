#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#


# @lc code=start
class Solution:

    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        m = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]
        if l1 * l2 == 0:
            return l1 + l2
        
        for i in range(l1 + 1):
            m[i][0] = i

        for j in range(l2 + 1):
            m[0][j] = j

        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                left = m[i - 1][j] + 1
                down = m[i][j - 1] + 1
                left_down = m[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    left_down += 1
                m[i][j] = min(left, down, left_down)
        return m[l1][l2]


# @lc code=end
