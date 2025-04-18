#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#
from typing import List
# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        max_height = 0
        while left < right:
            h = min(height[left], height[right])
            if h > max_height:
                max_area = max(h * (right - left), max_area)
                max_height = h
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
# @lc code=end
