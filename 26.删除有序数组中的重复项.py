#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#
from typing import List
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 0, 1
        l = len(nums)
        if l < 2:
            return l
        while right < l:
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
            right += 1
        return left + 1
    
nums = [1,1,2]
Solution().removeDuplicates(nums)
# @lc code=end

