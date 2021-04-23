#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
# https://leetcode-cn.com/problems/reverse-integer/description/
#
# algorithms
# Easy (35.00%)
# Likes:    2657
# Dislikes: 0
# Total Accepted:    635.4K
# Total Submissions: 1.8M
# Testcase Example:  '123'
#
# 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
# 
# 如果反转后整数超过 32 位的有符号整数的范围 [−2^31,  2^31 − 1] ，就返回 0。
# 假设环境不允许存储 64 位整数（有符号或无符号）。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：x = 123
# 输出：321
# 
# 
# 示例 2：
# 
# 
# 输入：x = -123
# 输出：-321
# 
# 
# 示例 3：
# 
# 
# 输入：x = 120
# 输出：21
# 
# 
# 示例 4：
# 
# 
# 输入：x = 0
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# -2^31 
# 
# 
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        max_val = (1<<31) - 1
        min_val = - 1<<31 
        # str_x = str(x)
        # if str_x[0] != '-':
        #     str_x = str_x[::-1]
        #     x = int(str_x)
        # else:
        #     str_x = str_x[:0:-1]
        #     x= int(str_x)
        #     x = -x
        # return x if min_val < x < max_val else 0
        # -123 % 10 = -123 - (10*(-13)) = 7
        # -123 // 10 = -12.3 向下取整 -13
        # 如果 x 是 -2147483648 ，abs（x）后 y= 2147483648已经超出正整数的存储范围
        if x == min_val:
            return 0
        y, res = abs(x), 0
        # 则其数值范围为 [−2^31,  2^31 − 1]
        boundry = (1<<31) -1 
        while y != 0:
            tmp = y % 10
            if res > max_val//10 or (res == max_val//10 and tmp > 7):
                return 0
            res = res*10 + tmp
            y //= 10
        return res if x > 0 else -res

# @lc code=end

