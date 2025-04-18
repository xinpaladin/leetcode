#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#
from typing import List


# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l1, l2 = m - 1, n - 1
        cur = m + n - 1
        while l1 >= 0 and l2 >= 0:
            if l1 == -1:
                nums1[cur] = nums2[l2]
                l2 -= 1
            elif l2 == -1:
                nums1[cur] = nums1[l1]
                l1 -= 1
            elif nums1[l1] < nums2[l2]:
                nums1[cur] = nums2[l2]
                l2 -= 1
            else:
                nums1[cur] = nums1[l1]
                l1 -= 1
            cur -= 1


nums1 = [4, 5, 6, 0, 0, 0]
nums2 = [1, 2, 3]
m, n = 3, 3
Solution().merge(nums1, m, nums2, n)
print(nums1)
# @lc code=end
