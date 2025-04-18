#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#
import re
# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split('/')
        new_path = []
        for i in path_list:
            if i == '..':
                if new_path:
                    new_path.pop() 
            elif i == '.' or i == '':
                pass
            else:
                new_path.append(i)
        return '/' + '/'.join(new_path)
# @lc code=end

# path = "/home/user/Documents/../Pictures"
# res = Solution().simplifyPath(path)
