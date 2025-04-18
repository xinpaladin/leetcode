#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#


# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 用了除法不符合
        # total = 1
        # extra = {}
        # l = len(nums)
        # answer = [0] * l
        # for i in range(l):
        #     if nums[i] == 0:
        #         extra[i] = 0
        #         continue
        #     total = total * nums[i]

        # if len(extra) >= 2:
        #     return answer

        # for i in range(l):
        #     if not extra or (extra and i in extra):
        #         answer[i] = int(total / nums[i])
        # return answer


        # l = len(nums)
        # L, R, answer = [0] * l, [0] * l, [0] * l
        # L[0] = 1
        # for i in range(1, l):
        #     L[i] = L[i - 1] * nums[i - 1]
        # R[l - 1] = 1
        # for j in range(l - 2, -1, -1):
        #     R[j] = R[j + 1] * nums[j + 1]

        # for a in range(l):
        #     answer[a] = L[a] * R[a]
        # return answer
        
        l = len(nums)
        answer = [0] * l
        answer[0] = 1
        
        for i in range(1, l):
            answer[i] = answer[i - 1] * nums[i - 1]
        
        R = 1
        for i in range(l-2, -1, -1):
            R *= nums[i+1]
            answer[i] = answer[i] * R
            
        return answer
# @lc code=end
