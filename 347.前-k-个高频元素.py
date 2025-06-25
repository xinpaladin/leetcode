#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#
from typing import List
# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # d = {}
        # for num in nums:
        #     d[num] = d.get(num, 0) + 1
        # import heapq 
        # l = []
        # for val, freq in d.items():
        #     if len(l) < k:
        #         heapq.heappush(l , (freq, val))
        #     else:
        #         heapq.heappushpop(l, (freq, val))
        # return [val for _, val in l]

        # 桶排序
        # 时间复杂度：O(n)，其中 n 是 nums 的长度。
        # 空间复杂度：O(n)
        # 第一步：统计每个元素的出现次数
        # from collections import Counter
        # cnt = Counter(nums)
        # max_cnt = max(cnt.values())

        # # 第二步：把出现次数相同的元素，放到同一个桶中
        # buckets = [[] for _ in range(max_cnt + 1)]  # 也可以用 defaultdict(list)
        # for x, c in cnt.items():
        #     buckets[c].append(x)

        # # 第三步：倒序遍历 buckets，把出现次数前 k 大的元素加入答案
        # ans = []
        # for bucket in reversed(buckets):
        #     ans += bucket
        #     # 题目保证答案唯一，一定会出现恰好等于 k 的情况
        #     if len(ans) == k:
        #         return ans

        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1

        l = []
        for value, freq in d.items():
            l.append((freq, value))


        def quicksort(nums, k, res):
            import random
            big, equal, small = [], [], []
            partition = random.choice(nums)
            for num in nums:
                if num[0] == partition[0]:
                    equal.append(num)
                elif num[0] > partition[0]:
                    big.append(num)
                else:
                    small.append(num)
            if len(big) > k :
                return quicksort(big, k, res)
            elif k - len(big) - len(equal) > 0:
                res  += [ value for _, value in big] + [value for _, value in equal]
                return quicksort(small, k - len(big) - len(equal), res)
            res += [ value for _, value in big]
            for i in range(k-len(big)):
                res.append(equal[i][1])
            return res
        return quicksort(l, k, [])
nums = [1,1,1,2,2,3]
# nums.extend([1]*100)
# nums = [1,1,1,2,2,3333]
k = 2
for i in range(5):
    res = Solution().topKFrequent(nums, k)
    print(res)
# @lc code=end

