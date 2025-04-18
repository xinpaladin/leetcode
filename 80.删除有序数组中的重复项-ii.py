#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除有序数组中的重复项 II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # flag = False
        # num = None
        # i = 0
        # l = len(nums)
        # while i < l:
        #     if num is None or num != nums[i]:
        #         num = nums[i]
        #         flag = False
        #         i += 1
        #         continue
        #     if num == nums[i]:
        #         if not flag:
        #             flag = True
        #             i += 1
        #         else:
        #             del nums[i]
        #             l -= 1
        # return len(nums)
        n = len(nums)
        if n <= 2:
            return n
        
        slow, fast = 2, 2
        while fast < n:
            if nums[slow-2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
            
            
        
            
# @lc code=end

