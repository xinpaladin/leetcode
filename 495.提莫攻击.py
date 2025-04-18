#
# @lc app=leetcode.cn id=495 lang=python3
#
# [495] 提莫攻击
#



# @lc code=start
class Solution:
    def findPoisonedDuration(self, timeSeries, duration: int) -> int:
        t = 0
        end = -1
        for i in timeSeries:
            if i <= end:
                if i + duration > end:
                    t += i + duration - end - 1
                    end = i + duration - 1
            else:
                t += duration
                end = i + duration - 1
            # print(t, end)
        return t

# timeSeries = [1,2,3,4,5]
# duration = 5
# print(Solution().findPoisonedDuration(timeSeries, duration))

# @lc code=end
