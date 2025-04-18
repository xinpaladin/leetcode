#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# from typing import Optional
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        small_head = ListNode(0)
        small_cur = small_head
        big_head = ListNode(0)
        big_cur = big_head
        cur = head
        while cur:
            if cur.val >= x:
                big_cur.next = cur
                big_cur = big_cur.next
            else:
                small_cur.next = cur
                small_cur = small_cur.next
            cur = cur.next

        big_cur.next = None
        small_cur.next = big_head.next
        return small_head.next
    
# def init_head(l):
#     head = None
#     cur = None
#     for i in l:
#         node = ListNode(i)
#         if not head:
#             head = node
#             cur = node
#         else:
#             cur.next = node
#             cur = cur.next
#     return head

# head = init_head([1,4,3,2,5,2])
# x = 3
# Solution().partition(head, x)
# @lc code=end

