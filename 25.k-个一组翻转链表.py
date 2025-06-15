#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverse(self, head: ListNode, tail: ListNode):
        pre = tail.next
        p = head
        while pre  != tail:
            next = p.next
            p.next = pre
            pre = p
            p = next
        return tail, head


    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        hair = ListNode(0, head)
        pre = hair
        cur = head
        while cur:
            tail = pre
            # 查看剩余部分长度是否大于等于 k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            next = tail.next
            cur, tail = self.reverse(cur, tail)
            
            pre.next = cur
            tail.next = next
            pre = tail
            cur = tail.next
        return hair.next


# @lc code=end
