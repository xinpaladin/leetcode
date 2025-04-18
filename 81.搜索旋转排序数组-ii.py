#
# @lc app=leetcode.cn id=81 lang=python3
#
# [81] 搜索旋转排序数组 II
#
from typing import List
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        if nums[0] == target or nums[-1] == target:
            return True 
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return True
            if nums[l] == nums[mid] and nums[r] == nums[mid]:
                l += 1
                r -= 1
            elif nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False
# @lc code=end
nums = [1,0,1,1,1]
target = 0
Solution().search(nums, target)