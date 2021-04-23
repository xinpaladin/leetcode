#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            return self.addBinary(b, a)
        l1, l2 = len(a) -1 , len(b)-1
        new = ''
        add = 0
        while l1 >=0 or l2 >= 0:
            a_val = int(a[l1]) if l1 >=0 else 0
            b_val = int(b[l2]) if l2 >=0 else 0
            tmp = a_val + b_val + add
            add = tmp // 2
            new = str(tmp%2) + new
            l1 -= 1
            l2 -= 1
        if add > 0:
            new = str(add) + new
        return new
# @lc code=end

