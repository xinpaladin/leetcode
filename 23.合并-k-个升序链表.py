#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并 K 个升序链表
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
ListNode.__lt__ = lambda a, b: a.val < b.val 
class Solution:
    def mergeTwoLists(self, head1: Optional[ListNode], head12: Optional[ListNode]):
        new_head = ListNode()
        cur, index1, index2 = new_head, head1, head12
        while index1 and index2:
            if index1.val > index2.val:
                cur.next = index2
                index2 = index2.next
            else:
                cur.next = index1
                index1 = index1.next
            cur = cur.next
        cur.next = index1 if index1 else index2
        return new_head.next

    # 分治
    def merge(self, lists: List[Optional[ListNode]], l: int, r: int):
        if l == r:
            return lists[l]
        if l > r:
            return None
        mid = (l + r) // 2
        return self.mergeTwoLists(
            self.merge(lists, l, mid), self.merge(lists, mid + 1, r)
        )

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l = len(lists)
        if l == 1:
            return lists[0]
        if not lists:
            return None
        # 暴力解法，时间复杂度O(k^2n)
        # head1 = lists[0]
        # for i in range(1, l):
        #     head1 = self.mergeTwoLists(head1, lists[i])
        # return head1

        # 优化1 分治
        # return self.merge(lists, 0, l - 1)


        # 最小堆
        from heapq import heapify, heappop, heappush
        cur = dummy = ListNode()  # 哨兵节点，作为合并后链表头节点的前一个节点
        h = [head for head in lists if head]  # 把所有非空链表的头节点入堆
        heapify(h)  # 堆化
        while h:  # 循环直到堆为空
            node = heappop(h)  # 剩余节点中的最小节点
            if node.next:  # 下一个节点不为空
                heappush(h, node.next)  # 下一个节点有可能是最小节点，入堆
            cur.next = node  # 把 node 添加到新链表的末尾
            cur = cur.next  # 准备合并下一个节点
        return dummy.next  # 哨兵节点的下一个节点就是新链表的头节点



# @lc code=end
