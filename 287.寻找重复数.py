#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#

from typing import List
# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 时间复杂度O(nlogn) 空间复杂度O(1)
        # n = len(nums)
        # l, r = 0, n-1
        # ans = -1
        # while l <= r:
        #     mid = (l+r)//2
        #     count = 0
        #     for i in range(n):
        #         if nums[i] <= mid:
        #             count += 1
        #     if count <= mid:
        #         l = mid +1
        #     else:
        #         r = mid -1
        #         ans = mid
        # return ans

        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                break
        return slow
    

# @lc code=end
