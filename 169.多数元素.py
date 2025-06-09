#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = len(nums)
        res = nums[0]
        count = 1

        for i in range(1,l):
            if count == 0:
                res = nums[i]
                count = 1
                continue
            if nums[i] == res:
                count += 1
            else:
                count -= 1

        return res
# @lc code=end

