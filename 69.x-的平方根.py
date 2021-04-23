#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x ==0 or x ==1 :
            return x 
        begin, end = 0, x
        anx = -1
        while begin <= end:
            mid = (begin + end)//2
            if mid * mid <= x:
                ans = mid
                begin = mid+1
            else:
                end = mid - 1
        return ans

# @lc code=end

