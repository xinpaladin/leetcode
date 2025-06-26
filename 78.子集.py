#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#
from typing import List


# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # res = []
        # n = len(nums)

        # for i in range(1 << n):
        #     tmp = []
        #     for j in range(n):
        #         if ((i >> j) & 1) > 0:
        #             tmp.append(nums[j])
        #     res.append(tmp)
        # return res
        res = [[]]
        for i in range(len(nums)):
            for j in range(len(res)):
                res.append(res[j]+[nums[i]])
        return res
# @lc code=end
nums = [1, 2, 3]
Solution().subsets(nums)
