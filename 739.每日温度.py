#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#

from typing import List


# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # l = len(temperatures)
        # t = [l - 1]
        # res = [0] * l
        # i = l - 2
        # while i >= 0:
        #     temperature = temperatures[i]
        #     t_l = len(t)
        #     j = t_l - 1
        #     while j >= 0:
        #         index = t[j]
        #         if temperatures[index] > temperature:
        #             res[i] = index - i
        #             break
        #         else:
        #             t.pop()
        #         j -= 1
        #     else:
        #         t = []
        #     t.append(i)
        #     i -= 1
        # return res
        length = len(temperatures)
        ans = [0] * length
        stack = []
        for i in range(length):
            temperature = temperatures[i]
            while stack and temperature > temperatures[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
            stack.append(i)
        return ans



Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
# @lc code=end
