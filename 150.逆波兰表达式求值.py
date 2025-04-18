#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#
from typing import List


# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: b - a,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(b / a),
        }
        flag = ["+", "-", "*", "/"]
        l = list()
        for token in tokens:
            if token in operations:
                num1 = l.pop()
                num2 = l.pop()
                l.append(operations[token](num1, num2))
            else:
                l.append(int(token))
        return l[0]


# @lc code=end

