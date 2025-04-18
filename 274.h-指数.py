#
# @lc app=leetcode.cn id=274 lang=python3
#
# [274] H 指数
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # h = len(citations)
        # while h > 0:
        #     count = 0
        #     for i in citations:
        #         if i >= h:
        #             count += 1
        #     if count >= h:
        #         return h
        #     else:
        #         h -= 1
        # return h

        # sorted_citations = sorted(citations, reverse=True)
        # h,i,n = 0,0,len(citations)
        # while i < n and sorted_citations[i] > h:
        #     h += 1
        #     i += 1
        # return h
        
        n = len(citations)
        counter = [0] * (n+1)
        for c in citations:
            if c >= n:
                counter[n] += 1
            else:
                counter[c] += 1
        
        tot = 0
        for i in range(n,-1, -1):
            
            tot += counter[i]
            if tot >= i:
                return i
        return 0
# @lc code=end

