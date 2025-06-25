#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
from typing import List
# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 堆排序
        # pq = []
        # for num in nums:
        #     heapq.heappush(pq, num)
        #     if len(pq)>k:
        #         heapq.heappop(pq)
        # return pq[0]

        # 快速排序
        # def swap(i: int, j: int) -> None:
        #     nums[i], nums[j] = nums[j], nums[i]
        
        # # 在[left, right]范围元素中进行降序快排，找到第k大元素
        # def quick_sort_kth_element(k: int, left: int, right: int) -> int:
        #     mid = (left+right)//2
        #     # 将切分值放到右边界避免加入元素的划分
        #     swap(mid, right)
        #     # 双指针从左右边界开始，分别找到要交换的元素
        #     partition, i, j = nums[right], left, right
        #     while i < j:
        #         while i<j and nums[i]>= partition: i+=1
        #         while i<j and nums[j]<= partition: j-=1
        #         if i < j:
        #             # 将大于元素放到左侧，小于元素放到右侧
        #             swap(i,j)
        #             i+=1
        #             j-=1
        #     # i最后停留的位置一定是右侧首个小于切分值的元素，与切分值交换，则[left, i)都是大于（等于）切分值，
        #     # [i+1, right]都是小于（等于）切分值
        #     swap(i, right)
        #     # 如果切分值就是第k大元素，直接返回
        #     if i == k-1: 
        #         return nums[i]
        #     # 切分值是第k大之前的元素，在右区间搜索第k大
        #     elif i < k-1: 
        #         return quick_sort_kth_element(k, i+1, right)
        #     else: 
        #         return quick_sort_kth_element(k, left, i - 1)

        # return quick_sort_kth_element(k, 0, len(nums)-1)
        def quick_select(nums, k):
            privot = random.choice(nums)
            small, equal, big = [], [], []
            for num in nums:
                if num < privot:
                    small.append(num)
                elif num > privot:
                    big.append(num)
                else:
                    equal.append(num)
            if k <= len(big):
                return quick_select(big, k)
            if k>len(big)+len(equal):
                return quick_select(small, k - len(big) - len(equal))
            return privot

        return quick_select(nums, k)

nums = [3,2,1,5,6,4]
k = 2

Solution().findKthLargest(nums, k)
# @lc code=end

