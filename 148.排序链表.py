#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        归并排序 递归，时间复杂度O(nlogn)
        空间复杂度：O(logn)，其中 n 是链表的长度。空间复杂度主要取决于递归调用的栈空间
        """
        # if not head or not head.next:
        #     return head

        # slow, fast = head, head.next
        # while fast and fast.next:
        #     fast = fast.next.next
        #     slow = slow.next

        # mid, slow.next = slow.next, None
        # # 递归排序
        # left, right = self.sortList(head), self.sortList(mid)
        # # 合并链表
        # cur = new_head = ListNode()
        # while left and right:
        #     if left.val < right.val:
        #         cur.next = left
        #         left = left.next
        #     else:
        #         cur.next = right
        #         right = right.next
        #     cur = cur.next
        # cur.next = left if left else right
        # return new_head.next

        """
        归并排序 迭代，时间复杂度O(nlogn)
        空间复杂度：O(1)
        """
        cur, length, intv = head, 0, 1
        while cur:
            cur = cur.next
            length += 1

        new_head = ListNode(next=head)

        while intv < length:
            pre, cur = new_head, new_head.next
            while cur:
                #
                h1, i = cur, intv
                while i and cur:
                    cur = cur.next
                    i -= 1
                if i:
                    break

                h2, i = cur, intv
                while i and cur:
                    cur = cur.next
                    i -= 1
                c1, c2 = intv, intv - i
                # merge h1 h2
                while c1 and c2:
                    if h1.val < h2.val:
                        pre.next = h1
                        h1 = h1.next
                        c1 -= 1
                    else:
                        pre.next = h2
                        h2 = h2.next
                        c2 -= 1
                    pre = pre.next
                pre.next = h1 if c1 else h2
                # 将pre指向已排序的尾部
                while c1 > 0 or c2 > 0:
                    pre = pre.next
                    c1 -= 1
                    c2 -= 1
                pre.next = cur
            intv *= 2
        return new_head.next


# @lc code=end
