#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#
# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (39.08%)
# Likes:    3413
# Dislikes: 0
# Total Accepted:    289.3K
# Total Submissions: 740.2K
# Testcase Example:  '[1,3]\n[2]'
#
# 给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。
#
# 进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？
#
#
#
# 示例 1：
#
# 输入：nums1 = [1,3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1,2,3] ，中位数 2
#
#
# 示例 2：
#
# 输入：nums1 = [1,2], nums2 = [3,4]
# 输出：2.50000
# 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
#
#
# 示例 3：
#
# 输入：nums1 = [0,0], nums2 = [0,0]
# 输出：0.00000
#
#
# 示例 4：
#
# 输入：nums1 = [], nums2 = [1]
# 输出：1.00000
#
#
# 示例 5：
#
# 输入：nums1 = [2], nums2 = []
# 输出：2.00000
#
#
#
#
# 提示：
#
#
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6
#
#
#


# @lc code=start
class Solution:

    def findMedianSortedArrays(self, nums1, nums2):
        # 确保nums1是较短的数组
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        imin, imax, half_len = 0, m, (m + n + 1) // 2

        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            # 处理边界条件
            if i < m and nums2[j - 1] > nums1[i]:
                # i太小，需要增大
                imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                # i太大，需要减少
                imax = i - 1
            else:
                # 找到合适的分割线，处理中位数计算
                # 计算左半部分最大值
                if i == 0:
                    max_of_left = nums2[j - 1]
                elif j == 0:
                    max_of_left = nums1[i - 1]
                else:
                    max_of_left = max(nums1[i - 1], nums2[j - 1])
                if (m + n) % 2 == 1:
                    return max_of_left
                # 计算右半部分最小值
                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])
                return (max_of_left + min_of_right) / 2.0

    def findMedianSortedArrays1(self, nums1, nums2):
        def getKthElement(k):
            """
            - 主要思路：要找到第 k (k>1) 小的元素，那么就取 pivot1 = nums1[k/2-1] 和 pivot2 = nums2[k/2-1] 进行比较
            - 这里的 "/" 表示整除
            - nums1 中小于等于 pivot1 的元素有 nums1[0 .. k/2-2] 共计 k/2-1 个
            - nums2 中小于等于 pivot2 的元素有 nums2[0 .. k/2-2] 共计 k/2-1 个
            - 取 pivot = min(pivot1, pivot2)，两个数组中小于等于 pivot 的元素共计不会超过 (k/2-1) + (k/2-1) <= k-2 个
            - 这样 pivot 本身最大也只能是第 k-1 小的元素
            - 如果 pivot = pivot1，那么 nums1[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums1 数组
            - 如果 pivot = pivot2，那么 nums2[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums2 数组
            - 由于我们 "删除" 了一些元素（这些元素都比第 k 小的元素要小），因此需要修改 k 的值，减去删除的数的个数
            """
            index1, index2 = 0, 0
            while True:
                if index1 == m:
                    # nums1已全部删除
                    return nums2[index2 + k - 1]
                if index2 == n:
                    # nums2已全部删除
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])
                newIndex1 = min(index1 + k // 2 - 1, m - 1)
                newIndex2 = min(index2 + k // 2 - 1, n - 1)
                pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
                if pivot1 <= pivot2:
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1
                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1

        m, n = len(nums1), len(nums2)
        totalLength = m + n
        if totalLength % 2 == 1:
            return getKthElement((totalLength + 1) // 2)
        else:
            return (
                getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)
            ) / 2


# a = [1,2,3,4,5,6]
# a = [1,2,3,4,5,6,7]
a = [3]
b = [-2, -1]
# # b = [7,8,9,10,11]
res = Solution().findMedianSortedArrays(a, b)
print(res)
# @lc code=end
