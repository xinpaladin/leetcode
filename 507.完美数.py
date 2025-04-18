#
# @lc app=leetcode.cn id=507 lang=python3
#
# [507] 完美数
#

# @lc code=start
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        sum = 1
        l, r = 2, num//2
        while l < r:
            if num % l == 0 and l != num:
                tmp = num // l
                sum += l
                sum += tmp
                r = tmp
            l += 1
        return num == sum
# @lc code=end

