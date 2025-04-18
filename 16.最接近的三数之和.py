#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#


# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # l = len(nums)
        # min_value = float("inf")
        # res = 0
        # for i in range(l - 2):
        #     for j in range(i + 1, l - 1):
        #         for k in range(j + 1, l):
        #             temp = abs(target - (nums[i] + nums[j] + nums[k]))
        #             if min_value > temp:
        #                 min_value = temp
        #                 res = nums[i] + nums[j] + nums[k]
        # return res
        l = len(nums)
        nums.sort()
        min_value = float("inf")
        res = float("inf")
        
        for i in range(l - 2):
            x = nums[i]
            if i > 0 and x == nums[i - 1]:
                continue
            
            # 优化一
            s = x + nums[i + 1] + nums[i + 2]
            if s > target:  # 后面无论怎么选，选出的三个数的和不会比 s 还小
                if s - target < min_value:
                    res = s  # 由于下一行直接 break，这里无需更新 min_diff
                break

            # 优化二
            s = x + nums[-2] + nums[-1]
            if s < target:  # x 加上后面任意两个数都不超过 s，所以下面的双指针就不需要跑了
                if target - s < min_value:
                    min_value = target - s
                    res = s
                continue

            li , ri = i+1, l -1
            while li < ri:
                s = nums[i] + nums[li] + nums[ri]
                v = abs(target - s)
                if min_value > v:
                    min_value = v
                    res = s
                if target > s:
                    li += 1
                elif target < s:
                    ri -= 1
                else:
                    return res
        return res
# @lc code=end
