#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head :
            return head
        new_head = ListNode(0, head)
        cur = new_head
        slow = head
        fast = head.next
        while slow and fast:

            slow.next = fast.next
            fast.next = slow
            cur.next = fast
            
            cur = slow 
            slow = slow.next
            fast = slow.next if slow and slow.next else None
        
        return new_head.next
            
# @lc code=end
