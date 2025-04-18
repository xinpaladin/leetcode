#
# @lc app=leetcode.cn id=482 lang=python3
#
# [482] 密钥格式化
#

# @lc code=start
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # s = s.replace('-', '').upper()
        # s_n = len(s)
        # si = s_n % k
        # new_s = s[:si] + '-' if si > 0 else ''
        # count = 0
        # while count < s_n // k:
        #     new_s += s[si+k*count: si+k*(count+1)] + '-'
        #     count += 1
        
        # return new_s[:-1]
        s = s.upper().replace('-', '')[::-1]
        res = ''
        for i in range(0, len(s), k):
            res += s[i:i+k] + '-'
        return res[::-1].lstrip('-')
# @lc code=end

