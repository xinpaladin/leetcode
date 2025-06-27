#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
# https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (56.30%)
# Likes:    1229
# Dislikes: 0
# Total Accepted:    246.9K
# Total Submissions: 438.3K
# Testcase Example:  '"23"'
#
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
#
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
#
#
#
#
#
# 示例 1：
#
#
# 输入：digits = "23"
# 输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
#
#
# 示例 2：
#
#
# 输入：digits = ""
# 输出：[]
#
#
# 示例 3：
#
#
# 输入：digits = "2"
# 输出：["a","b","c"]
#
#
#
#
# 提示：
#
#
# 0
# digits[i] 是范围 ['2', '9'] 的一个数字。
#
#
#


# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return list()

        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        # 第一种方法
        # groups = (phoneMap[digit] for digit in digits)
        # return ["".join(combination) for combination in itertools.product(*groups)]
        
        # 第二种回溯
        combinations = []

        # 每次递归会生成一个str,光一个str路径上按len=4
        # def backtrack(index, combination):
        #     if index == len(digits):
        #         combinations.append(combination)
        #     else:
        #         digit = digits[index]
        #         letters = phoneMap[digit]
        #         for i in letters:
        #             backtrack(index + 1, combination + i)
        # backtrack(0, "")


        # 第三种 回溯,从测试结果来看和第二章使用内存没区别
        combination = []
        def backtrack(index):
            if index == len(digits):
                combinations.append("".join(combination))
            else:
                digit = digits[index]
                for i in phoneMap[digit]:
                    combination.append(i)
                    backtrack(index + 1)
                    combination.pop()
        backtrack(0)


        return combinations


# @lc code=end
