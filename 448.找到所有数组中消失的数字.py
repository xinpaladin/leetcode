#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # return list(set(range(1, len(nums)+1)).difference(set(nums)))
        l = len(nums)
        for i in nums:
            tmp = i%l
            nums[tmp-1] += l
        res = []
        for i in range(l):
            if nums[i] <= l:
                res.append(i+1) 
        return res
# @lc code=end

