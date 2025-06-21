#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (42.34%)
# Likes:    965
# Dislikes: 0
# Total Accepted:    241.5K
# Total Submissions: 569.6K
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
#
# 如果数组中不存在目标值 target，返回 [-1, -1]。
#
# 进阶：
#
#
# 你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
#
#
#
#
# 示例 1：
#
#
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4]
#
# 示例 2：
#
#
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1]
#
# 示例 3：
#
#
# 输入：nums = [], target = 0
# 输出：[-1,-1]
#
#
#
# 提示：
#
#
# 0
# -10^9
# nums 是一个非递减数组
# -10^9
#
#
#


# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # if not nums or nums[0]>target or nums[-1]<target or target not in nums:
        #     return [-1, -1]
        # l,r = 0, len(nums)
        # start, end = None, None
        # while l < r:
        #     mid = (l+r) // 2
        #     if nums[mid] == target:
        #         start, end = mid, mid
        #         while start>0 and nums[start-1] == target :
        #             start -= 1
        #         while end < len(nums)-1 and nums[end+1] == target :
        #             end += 1
        #         return [start, end]
        #     elif nums[mid] > target:
        #         r = mid
        #     else:
        #         l = mid

        # return [-1, -1]
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def left_func(nums, target):
            left, right = 0, len(nums) -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid - 1
                if nums[mid] < target:
                    left = mid + 1
            return left

        a = left_func(nums, target)
        b = left_func(nums, target + 1)
        if a == len(nums) or nums[a] != target:
            return [-1, -1]
        else:
            return [a, b - 1]


# @lc code=end
