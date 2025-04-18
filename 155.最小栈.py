#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#
import math
# @lc code=start
class MinStack:

    def __init__(self):
        self.stack = list()
        self.min_stack = [math.inf]
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.pop()
