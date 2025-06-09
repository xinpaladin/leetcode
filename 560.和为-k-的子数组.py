#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#


# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 超时算法
        # res = 0
        # cur = 0
        # l = len(nums)
        # for i in range(l):
        #     cur += nums[i]
        #     if cur == k:
        #         res += 1
        #     begin = 0
        #     tmp = cur
        #     while begin < i:
        #         tmp -= nums[begin]
        #         begin += 1
        #         if tmp == k:
        #             res += 1
        # return res

        res = 0
        pre = 0
        pre_d = {0:1}
        l = len(nums)
        for i in range(l):
            pre += nums[i]
            if pre - k in pre_d:
                res += pre_d[pre - k]
            pre_d[pre] = pre_d.get(pre, 0) + 1

        return res
# @lc code=end
