#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:

    # def longestPalindrome(self, s: str) -> str:
    #     if len(s) < 2:
    #         return s

    #     l = ''
    #     def check(s: str):
    #         l, r = 0, len(s)-1
    #         while l < r:
    #             if s[l] != s[r]:
    #                 return False
    #             l += 1
    #             r -= 1
    #         return True

    #     for i in range(len(s)):
    #         for j in range(len(s), i,  -1):
    #             if len(l) >= len(s[i: j]):
    #                 break
    #             if check(s[i: j]) and len(l) < len(s[i: j]):
    #                 l = s[i: j]
    #     return l

    # 中心扩散
    # def expandAroundCenter(self, s, left, right):
    #     while left >= 0 and right < len(s) and s[left] == s[right]:
    #         left -= 1
    #         right += 1
    #     return left + 1, right - 1

    # def longestPalindrome(self, s: str) -> str:
    #     start, end = 0, 0
    #     for i in range(len(s)):
    #         left1, right1 = self.expandAroundCenter(s, i, i)
    #         left2, right2 = self.expandAroundCenter(s, i, i + 1)
    #         if right1 - left1 > end - start:
    #             start, end = left1, right1
    #         if right2 - left2 > end - start:
    #             start, end = left2, right2
    #     return s[start: end + 1]
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        max_len = 1
        begin = 0
        # dp[i][j] 表示 s[i..j] 是否是回文串
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        for L in range(2, n + 1):
            for i in range(n):
                # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
                j = L + i - 1
                # 如果右边界越界，就可以退出当前循环
                if j >= n:
                    break
                    
                # if s[i] != s[j]:
                #     dp[i][j] = False 
                # else:
                #     if j - i < 3:
                #         dp[i][j] = True
                #     else:
                #         dp[i][j] = dp[i + 1][j - 1]
                
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False 

                # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
        return s[begin : begin + max_len]


# @lc code=end

