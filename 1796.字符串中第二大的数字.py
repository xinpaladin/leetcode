#
# @lc app=leetcode.cn id=1796 lang=python3
#
# [1796] 字符串中第二大的数字
#


# @lc code=start
class Solution:
    def secondHighest(self, s: str) -> int:
        # max_n = -1
        # sec_max_n = -1

        # for i in s:
        #     if not i.isdigit():
        #         continue
        #     v = int(i)

        #     if v > max_n:
        #         sec_max_n = max_n
        #         max_n = v
        #     elif sec_max_n < v < max_n:
        #         sec_max_n = v
        # return sec_max_n
        
        # nums = set()
        # for i in s:
        #     if i.isdigit():
        #         nums.add(int(i))

        # nums = sorted(list(nums))
        # return nums[-2] if len(nums) > 1 else -1
        
        flag = False
        for i in range(9, -1, -1):
            if str(i) in s:
                if not flag:
                    flag = True
                else:
                    return i
        return -1


# @lc code=end
