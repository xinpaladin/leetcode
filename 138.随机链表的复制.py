#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 随机链表的复制
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''
        1. 在原链中复制节点
        2. 复制random关系
        3. 拆解链
        '''
        # cur = head
        # while cur:
        #     node = Node(cur.val, cur.next)
        #     cur.next = node
        #     cur = node.next

        # cur = head
        # while cur:
        #     cur.next.random = cur.random.next if cur.random else None
        #     cur = cur.next.next

        # new_head = Node(-1)
        # cur, new_cur = head, new_head
        # while cur:
        #     new_cur.next = cur.next
        #     cur = cur.next.next
        #     new_cur = new_cur.next

        # return new_head.next

        '''
        使用hash 存储新旧节点的关系
        '''
        if not head: return
        d = {}
        cur = head
        while cur:
            d[cur] = Node(cur.val)
            cur = cur.next
        new_head = d[head]
        cur, new_cur = head, new_head
        while cur:
            new_cur.next = d[cur.next] if cur.next else None
            new_cur.random = d[cur.random] if cur.random else None
            cur = cur.next
            new_cur = new_cur.next
        return new_head
# @lc code=end

