#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#
# https://leetcode-cn.com/problems/remove-linked-list-elements/description/
#
# algorithms
# Easy (46.50%)
# Likes:    516
# Dislikes: 0
# Total Accepted:    126.1K
# Total Submissions: 269.2K
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# 删除链表中等于给定值 val 的所有节点。
# 
# 示例:
# 
# 输入: 1->2->6->3->4->5->6, val = 6
# 输出: 1->2->3->4->5
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        pre = None
        cur = head
        while cur :
            if cur.val == val:
                if not pre:
                    head = head.next
                else:
                    pre.next = cur.next
                cur = cur.next
            else:
                pre = cur
                cur = cur.next
        return head
# @lc code=end

