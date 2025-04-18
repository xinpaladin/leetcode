#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#
from typing import List
# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        begin, end = 0, len(nums) -1 
        while begin < end:
            if nums[begin] == val:
                nums[begin] = nums[end]
                end -= 1
            else:
                begin += 1
        return begin
    
nums = [0,1,2,2,3,0,4,2]
val = 2
Solution().removeElement(nums, val)
# @lc code=end

