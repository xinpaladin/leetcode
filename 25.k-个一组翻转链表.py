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
    
    def reverse(head: ListNode, tail: ListNode):
        # prev = tail.next
        # p = head
        # while prev != tail:
        #     nex = p.next
        #     p.next = prev
        #     prev = p
        #     p = nex
        # return tail, head
        pre = tail.next
        p = head
        while pre != tail:
            nex = p.next
            p.next = pre
            pre = p
            p = nex
            
        return tail, head


    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        hair = ListNode(0)
        hair.next = head
        pre = hair
        while head:
            tail = pre
            # 查看剩余部分长度是否大于等于 k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nex = tail.next
            head, tail = self.reverse(head, tail)
            
            pre.next = head
            tail.next = nex
            pre = tail
            head = tail.next
        return hair.next


# @lc code=end
