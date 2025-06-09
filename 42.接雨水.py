#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

from typing import List
# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        # n = len(height)
        # res = 0
        # if n < 3:
        #     return res
        # left_max = [height[0]] + [0] * (n - 1)
        # for i in range(1, n):
        #     left_max[i] = max(left_max[i - 1], height[i])

        # right_max = [0] * (n - 1) + [height[n - 1]]
        # for i in range(n - 2, -1, -1):
        #     right_max[i] = max(right_max[i + 1], height[i])

        # res = sum(min(left_max[i], right_max[i]) - height[i] for i in range(n))
        # return res

        # 双指针
        ans = 0
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if height[left] < height[right]:
                ans += left_max - height[left]
                left += 1
            else:
                ans += right_max - height[right]
                right -= 1
        return ans
# @lc code=end

# height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Solution().trap(height)
