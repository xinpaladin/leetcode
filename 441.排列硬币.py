#
# @lc app=leetcode.cn id=441 lang=python3
#
# [441] 排列硬币
#

# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
        # if n < 3:
        #     return 1
        # line = 0
        # while line*(line+1)/2 <= n:
        #     line += 1
        # return line - 1
        import math
        return int(math.sqrt(2*n+1.0/4) - 1.0/2)
# @lc code=end

