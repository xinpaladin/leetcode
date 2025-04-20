#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#

from typing import List


# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # n = len(gas)
        # i = 0
        # while i < n:
        #     sum_gas, sum_cost = 0, 0
        #     cnt = 0
        #     while cnt < n:
        #         j = (i + cnt) % n
        #         sum_gas += gas[j]
        #         sum_cost += cost[j]
        #         if sum_gas < sum_cost:
        #             break
        #         cnt += 1
        #     if cnt == n:
        #         return i
        #     else:
        #         i += cnt + 1
        # return -1
        if sum(gas) < sum(cost):
            return -1
        n = len(gas)
        l = 0
        r = 0
        cur_gas = gas[0] - cost[0]
        cnt = n-1
        while cnt > 0:
            if cur_gas >= 0:
                r += 1
                cnt-=1
                cur_gas += gas[r] - cost[r]

            else:
                l = (l - 1 + n) % n
                cnt-=1
                cur_gas += gas[l] - cost[l]
        return l


# gas = [1,2,3,4,5,5,70]
# cost = [2,3,4,3,9,6,2]
# res = Solution().canCompleteCircuit(gas, cost)
# print(res)
# @lc code=end
