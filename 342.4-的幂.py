#
# @lc app=leetcode.cn id=342 lang=python3
#
# [342] 4的幂
#
# https://leetcode-cn.com/problems/power-of-four/description/
#
# algorithms
# Easy (49.42%)
# Likes:    149
# Dislikes: 0
# Total Accepted:    35.1K
# Total Submissions: 71.1K
# Testcase Example:  '16'
#
# 给定一个整数，写一个函数来判断它是否是 4 的幂次方。如果是，返回 true ；否则，返回 false 。
# 
# 整数 n 是 4 的幂次方需满足：存在整数 x 使得 n == 4^x
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 16
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：n = 5
# 输出：false
# 
# 
# 示例 3：
# 
# 
# 输入：n = 1
# 输出：true
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
# 
# 进阶：
# 
# 
# 你能不使用循环或者递归来完成本题吗？
# 
# 
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # if n == 1:
        #     return True
        # if n < 0:
        #     return False
        # bin_str = bin(n)
        # if '0b1' in bin_str and (len(bin_str)-3)%2 == 0 and '1' not in bin_str[3:]:
        #     return True
        # return False
        return n > 0 and n & (n - 1) == 0 and n & 0xaaaaaaaa == 0
# @lc code=end

