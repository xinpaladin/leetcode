#
# @lc app=leetcode.cn id=373 lang=python3
#
# [373] 查找和最小的 K 对数字
#
from typing import List
import heapq
# @lc code=start
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        res = []
        h = [[nums1[i] + nums2[0], i, 0] for i in range(min(k, len(nums1)))]
        
        while len(res) < k:
            _, i, j = heapq.heappop(h)
            res.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(h, [nums1[i] + nums2[j+1], i, j+1])
        return res
# @lc code=end

# nums1 = [1,1,2]
# nums2 = [1,2,3]
# k = 2
# Solution().kSmallestPairs(nums1, nums2, k)