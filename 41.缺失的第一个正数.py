#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#


# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        n = len(nums)

        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1

        for i in range(n):
            num = abs(nums[i])
            if num < n + 1:
                nums[num - 1] = -abs(nums[num - 1])

        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1


# @lc code=end
