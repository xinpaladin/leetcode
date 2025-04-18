#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s, g = sorted(s, reverse=True), sorted(g, reverse=True)
        res = 0
        i,j = 0, 0
        s_n, g_n = len(s), len(g)
        while i < s_n and j < g_n:
            if s[i] >= g[j]:
                i += 1
                res += 1

            j += 1
        return res
# @lc code=end

