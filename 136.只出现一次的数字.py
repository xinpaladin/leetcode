#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#
from functools import reduce

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 时间复杂度O(n) 空间复杂度O(n) 
        # d = {}
        # for num in nums:
        #     d[num] = d.get(num, 0) + 1

        # for k, v in d.items():
        #     if v == 1:
        #         return k

        return reduce(lambda x,y: x ^ y, nums)


# @lc code=end
