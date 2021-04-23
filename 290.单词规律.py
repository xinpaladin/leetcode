#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#
# https://leetcode-cn.com/problems/word-pattern/description/
#
# algorithms
# Easy (43.84%)
# Likes:    213
# Dislikes: 0
# Total Accepted:    35.3K
# Total Submissions: 80.5K
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# 给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。
# 
# 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。
# 
# 示例1:
# 
# 输入: pattern = "abba", str = "dog cat cat dog"
# 输出: true
# 
# 示例 2:
# 
# 输入:pattern = "abba", str = "dog cat cat fish"
# 输出: false
# 
# 示例 3:
# 
# 输入: pattern = "aaaa", str = "dog cat cat dog"
# 输出: false
# 
# 示例 4:
# 
# 输入: pattern = "abba", str = "dog dog dog dog"
# 输出: false
# 
# 说明:
# 你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。    
# 
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ss = s.split(' ')
        DIC = {}
        if len(pattern) != len(ss):
            return False

        def judge(s1, s2):
            DIC = {}
            for i in range(len(s1)):
                if s1[i] in DIC:
                    if DIC[s1[i]] != s2[i]:
                        return False
                else:
                    DIC[s1[i]] = s2[i]
            return True
        return judge(pattern, ss) and judge(ss,pattern)
# @lc code=end

