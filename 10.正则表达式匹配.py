#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#
# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 动态规划
        m, n = len(s), len(p)
        
        def matches(i: int, j: int) -> bool:
            if i == 0:
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]


        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    f[i][j] |= f[i][j - 2]
                    if matches(i, j - 1):
                        f[i][j] |= f[i - 1][j]
                else:
                    if matches(i, j):
                        f[i][j] |= f[i - 1][j - 1]
        return f[m][n]


        
        # 暴力破解
        # if '.' not in p and '*' not in p:
        #     return s == p
        # si = pi = 0
        # sl, pl = len(s), len(p)
        # while pi < pl:
        #     if pi + 1 < pl and p[pi+1] == '*':
        #         ss = p[pi]
        #         pi += 2
                
        #         if pi >= pl:
                    
        #             while si < sl:
        #                 if ss == '.' or s[si] == ss:
        #                     si += 1
        #                 else:
        #                     return False
        #             return True 
        #         else:
        #             res = False
        #             while si < sl:
        #                 res = self.isMatch(s[si:], p[pi:])
        #                 if res == True:
        #                     return True
        #                 if s[si] == ss or ss == '.':
        #                     si += 1
        #                 else:
        #                     return False
        #     else:
        #         if si >= sl:
        #             return False 
        #         if s[si] != p[pi] and p[pi]!='.':
        #             return False
        #         else:
        #             si += 1
        #             pi += 1
        # return si == sl and pi == pl
# @lc code=end

# print(Solution().isMatch("ab", 'a*'))
# print(Solution().isMatch("aaa", 'a*a'))
# print(Solution().isMatch("b", 'ba*'))
# print(Solution().isMatch("ab", '.*c'))
# print(Solution().isMatch("aa", 'a*'))
# print(Solution().isMatch("aab", 'aa*b'))
# print(Solution().isMatch("aab", 'aab'))
# print(Solution().isMatch("aab", 'ab'))
# print(Solution().isMatch("mississippi","mis*is*p*."))
# @lc code=end

