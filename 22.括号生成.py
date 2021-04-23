#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
# https://leetcode-cn.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (77.01%)
# Likes:    1737
# Dislikes: 0
# Total Accepted:    262.4K
# Total Submissions: 340.5K
# Testcase Example:  '3'
#
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
#
#
# 示例 1：
#
#
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
#
#
# 示例 2：
#
#
# 输入：n = 1
# 输出：["()"]
#
#
#
#
# 提示：
#
#
# 1
#
#
#


# @lc code=start
class Solution:
    def generateParenthesis(self, n):

        results = set()

        def backtrace(res, left, right):
            if left == right == 0:
                results.add(res)
                return
            if left == 0:
                results.add(res + ')' * right)
                return
            if left == right:
                backtrace(res + '(', left - 1, right)
                return
            backtrace(res + '(', left - 1, right)
            backtrace(res + ')', left, right - 1)

        backtrace('', n, n)
        return list(results)


# @lc code=end
