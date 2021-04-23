#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#
# https://leetcode-cn.com/problems/excel-sheet-column-title/description/
#
# algorithms
# Easy (38.68%)
# Likes:    288
# Dislikes: 0
# Total Accepted:    38.8K
# Total Submissions: 100.2K
# Testcase Example:  '1'
#
# 给定一个正整数，返回它在 Excel 表中相对应的列名称。
# 
# 例如，
# 
# ⁠   1 -> A
# ⁠   2 -> B
# ⁠   3 -> C
# ⁠   ...
# ⁠   26 -> Z
# ⁠   27 -> AA
# ⁠   28 -> AB 
# ⁠   ...
# 
# 
# 示例 1:
# 
# 输入: 1
# 输出: "A"
# 
# 
# 示例 2:
# 
# 输入: 28
# 输出: "AB"
# 
# 
# 示例 3:
# 
# 输入: 701
# 输出: "ZY"
# 
# 
#

# @lc code=start
class Solution:
    def convertToTitle(self, n):
        # 26进制转换
        if n < 1:
            return ""
        res = ""
        while n > 26:
            tmp = n%26
            n = n // 26
            if tmp == 0:
                res = 'Z' + res
                n -= 1
            else:
                res = chr(tmp+64) + res
            
        res = chr(n+64) + res
        return res
# @lc code=end
