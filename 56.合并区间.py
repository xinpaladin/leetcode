#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
from typing import List


# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []
        for i in intervals:
            if not merged or merged[-1][1] < i[0]:
                merged.append(i)
            else:
                merged[-1][1] = max(merged[-1][1], i[1])
        return merged


        # nums = ["#"]
        # for i in range(10**4 + 1):
        #     nums.append("0")
        #     nums.append("#")

        # for i in intervals:
        #     if i[0] == i[1]:
        #         nums[2 * i[0] + 1] = "1"
        #     for j in range(i[0], i[1]):
        #         nums[2 * j + 1] = "1"
        #         nums[2 * j + 2] = "*"
                
        # new_intervals = []
        # f = False
        # start = 0
        # for i, n in enumerate(nums):
        #     if f and n == "#":
        #         new_intervals.append([start, i // 2 - 1])
        #         f = False
        #     if not f and n == "1":
        #         start = (i - 1) // 2
        #         f = True
        # return new_intervals



# @lc code=end
