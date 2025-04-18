#
# @lc app=leetcode.cn id=504 lang=python3
#
# [504] 七进制数
#

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        flag = True
        if num < 0:
            flag = False
            num = -num
        
        res= ''
        while num >= 7:
            tmp = num % 7
            res = f'{tmp}{res}'
            num = num // 7
        
        res = f'{num}{res}' if flag else f'-{num}{res}'
        return res 
        
# @lc code=end

