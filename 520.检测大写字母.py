#
# @lc app=leetcode.cn id=520 lang=python3
#
# [520] 检测大写字母
#


# @lc code=start
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # 均大写 或均小写
        # if word.lower() == word or word.upper() == word:
        #     return True

        # # 首字母小写
        # if word[0].lower() == word[0]:
        #     return False
        # else:
        #     # 首字母大写
        #     return word[1:].lower() == word[1:]
        
        return word.isupper() or word.islower() or word.istitle()
# @lc code=end
