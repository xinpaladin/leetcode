#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#
import heapq
import copy


# @lc code=start
class MedianFinder:

    # def __init__(self):
    #     self.data = []

    # def addNum(self, num: int) -> None:
    #     self.data.append(num)

    # def findMedian(self) -> float:
    #     # 找n//2 or n//2 n//2+1
    #     l = len(self.data)
    #     tmp = copy.copy(self.data)
    #     heapq.heapify(tmp)
    #     num1, num2 = None, None
    #     count = l //2
    #     while count > 0:
    #         num1 = heapq.heappop(tmp)
    #         count -= 1
    #     if l % 2 == 0:
    #         num2 = heapq.heappop(tmp)
    #         return (num1 + num2) / 2.0
    #     else:
    #         return heapq.heappop(tmp)

    # 维护两个堆， 左边为l//2的 右边为 l//2, 左边的值总是小于右边的值
    # 通过将左边的值取复数，是的左堆 pop的值为最大值
    def __init__(self):
        self.que_min = []
        self.que_max = []

    def addNum(self, num: int) -> None:
        que_min = self.que_min
        que_max = self.que_max

        if not que_min or num <= -que_min[0]:
            heapq.heappush(que_min, -num)
            if len(que_max) + 1 < len(que_min):
                heapq.heappush(que_max, -heapq.heappop(que_min))
        else:
            heapq.heappush(que_max, num)
            if len(que_max) > len(que_min):
                heapq.heappush(que_min, -heapq.heappop(que_max))

    def findMedian(self) -> float:
        que_max = self.que_max
        que_min = self.que_min
        if len(que_min) > len(que_max):
            return -que_min[0]
        return (-que_min[0] + que_max[0]) / 2.0
        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end
