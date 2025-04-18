#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
from typing import List
# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = - nums[i]
            right = n - 1
            for j in range(i+1, n-1):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                
                while j < right and nums[j] + nums[right] > target:
                    right -= 1
                if j == right:
                    break
                
                if nums[j] + nums[right] == target:
                    res.append([nums[i], nums[j], nums[right]])
        return res
# @lc code=end

nums = [-1,0,1,2,-1,-4]
print(Solution().threeSum(nums))
