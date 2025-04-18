#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # n = len(nums)
        # if n <=1:
        #     return True
        # dp = [0] * n
        # dp[0] = 1
        # for i in range(n):
        #     if dp[i] == 0:
        #         continue
        #     else:
        #         tmp = nums[i]
        #         if tmp + i > n - 1:
        #             return True
        #         while tmp>0 : 
        #             dp[i+tmp] = 1
        #             tmp -= 1
        # return dp[-1] == 1
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(i + nums[i], rightmost)
                if rightmost >= n - 1:
                    return True
            else:
                return False
        return False
# @lc code=end

