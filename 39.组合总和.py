#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
from typing import List
import copy

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        combination = []
        n = len(candidates)

        def backtrack(index):
            sum_val = sum(combination)
            if target == sum_val:
                combinations.append(copy.copy(combination))
            for i in range(index, n):
                if target >= sum_val + candidates[i]:
                    combination.append(candidates[i])
                    backtrack(i)
                    combination.pop()


        backtrack(0)
        return combinations


# @lc code=end

candidates = [2, 3, 6, 7]
target = 7
Solution().combinationSum(candidates, target)
