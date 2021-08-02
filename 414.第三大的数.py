#
# @lc app=leetcode.cn id=414 lang=python3
#
# [414] 第三大的数
#

# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        l = len(nums)
        if l <= 2:
            return max(nums)

        first = second = third = float('-inf')
        for num in nums:
            if num == first or num == second:
                continue

            if num > first:
                third = second
                second = first
                first = num
                continue
            
            if num > second:
                third = second
                second = num
                continue

            if num > third:
                third = num
        if third == float('-inf'):
            return first
        else:
            return third
        
# @lc code=end

