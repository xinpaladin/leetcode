#
# @lc app=leetcode.cn id=492 lang=python3
#
# [492] 构造矩形
#

# @lc code=start
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        import math
        W = int(math.sqrt(area))
        while area % W :
            W -= 1
        return [int(area/W), W]
# @lc code=end

