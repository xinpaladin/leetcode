#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#


# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        # l = len(nums)
        # dp = [float("inf")] * l
        # dp[0] = 0
        # j = 0
        # for i in range(1, l):
        #     while j + nums[j] < i:
        #         j += 1
        #     dp[i] = dp[j] + 1
        # return dp[l - 1]
        l = len(nums)
        max_pos, end, step = 0, 0, 0
        for i in range(l - 1):
            max_pos = max(max_pos, nums[i] + i)
            if i == end:
                end = max_pos
                step += 1
        return step


# @lc code=end
