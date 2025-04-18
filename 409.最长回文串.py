#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for i in s:
            d[i] = d.get(i, 0) + 1
            
        is_has_odd = False
        l = 0
        for v in d.values():
            if v % 2 == 1:
                if is_has_odd:
                    l += v - 1
                else:
                    l += v
                    is_has_odd = True
            else:
                l += v
        return l
            
# @lc code=end

