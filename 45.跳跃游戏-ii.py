#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#


# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        l = len(nums)
        dp = [float("inf")] * l
        dp[0] = 0
        j = 0
        for i in range(1, l):
            while j + nums[j] < i:
                j += 1
            dp[i] = dp[j] + 1 
        # for i, val in enumerate(nums):
        #     for j in range(1, val + 1):
        #         if i + j > l - 1:
        #             break
        #         if i + j == l - 1:
        #             return dp[i] + 1
        #         if dp[i + j] == -1:
        #             dp[i + j] = dp[i] + 1
        return dp[l - 1]
        # size = len(nums)
        # dp = [float("inf") for _ in range(size)]
        # dp[0] = 0

        # j = 0
        # for i in range(1, size):
        #     while j + nums[j] < i:
        #         j += 1
        #     dp[i] = dp[j] + 1

        # return dp[size - 1]

# @lc code=end
