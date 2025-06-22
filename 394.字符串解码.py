#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#


# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        # res_l = []
        # k_l, encoded_strs = [], []
        # tmp = []
        # for i in range(len(s)):

        #     if s[i] == "[":
        #         encoded_strs.append([])
        #         k_l.append(int(''.join(tmp)))
        #         tmp = []
        #     elif s[i].isdigit():
        #         tmp.append(s[i])
        #     elif s[i] == "]":
        #         k = k_l.pop()
        #         encoded_str = encoded_strs.pop()
        #         if k_l:
        #             encoded_strs[-1].append(k * "".join(encoded_str))
        #         else:
        #             res_l.append(k * "".join(encoded_str))
        #     else:
        #         if len(encoded_strs) == 0:
        #             res_l.append(s[i])
        #         else:
        #             encoded_strs[-1].append(s[i])
        # return "".join(res_l)
    
        #  官方精简代码
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':
                stack.append([multi, res])
                res, multi = "", 0
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)            
            else:
                res += c
        return res




# Solution().decodeString("3[a2[c]]")
# Solution().decodeString("3[a]2[bc]")
# Solution().decodeString("13[a]2[bc]")
# @lc code=end
