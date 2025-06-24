#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

from typing import List


# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Time Limit Exceeded
        # res = 0
        # min_heights = []
        # l = len(heights)
        # for i in range(l):
        #     if not min_heights:
        #         min_heights.append((i, heights[i]))
        #         res = heights[i]
        #     else:
        #         for j in min_heights:
        #             start_i, h = j
        #             tmp = (i - start_i + 1) * min(h, heights[i])
        #             res = max(tmp, res, heights[i])
        #         min_index = i
        #         while min_heights:
        #             start_i, h = min_heights.pop()
        #             if heights[i] > h:
        #                 min_heights.append((start_i, h))
        #                 break
        #             else:
        #                 min_index = start_i
        #         min_heights.append((min_index, heights[i]))
        # return res

        # 单调栈
        # n = len(heights)
        # # left i 位置左侧height > height[i]的最远边界，最远为 -1表示左侧边界
        # # right i 位置右侧height > height[i]的最远边界，最远为 n表示右侧边界

        # left, right = [0] * n, [0] * n

        # monstack = list()
        # for i in range(n):
        #     while monstack and heights[monstack[-1]] >= heights[i]:
        #         monstack.pop()
        #     left[i] = monstack[-1] if monstack else -1
        #     monstack.append(i)

        # monstack = list()
        # for i in range(n - 1, -1, -1):
        #     while monstack and heights[monstack[-1]] >= heights[i]:
        #         monstack.pop()
        #     right[i] = monstack[-1] if monstack else n
        #     monstack.append(i)

        # ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
        # return ans

        n = len(heights)
        left, right = [0] * n, [n] * n

        mono_stack = list()
        for i in range(n):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                right[mono_stack[-1]] = i
                mono_stack.pop()
            left[i] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)
        
        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
        return ans




# heights = [2, 1, 5, 6, 2, 3]
# heights = [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2]
# heights = [6,7,5,2,4,5,9,3]
# Solution().largestRectangleArea(heights)

# @lc code=end
