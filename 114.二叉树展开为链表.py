#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 时间复杂度 O(2n) 空间复杂度 O(n)
        # if not root:
        #     return
        # stack, nodes = [root], []
        # while stack:
            
        #     node = stack.pop()
        #     nodes.append(node)
        #     if node.right:
        #         stack.append(node.right)
        #     if node.left:
        #         stack.append(node.left)

        # l = len(nodes)
        # for i in range(l-1):
        #     nodes[i].left = None
        #     nodes[i].right = nodes[i+1]
        

        # 第二种写法， 空间又节省一些， 空间复杂度依然是 O(n)
        # if not root:
        #     return 
        
        # stack, prev = [root], None
        # while stack:
        #     node = stack.pop()
        #     left, right = node.left, node.right
        #     if prev:
        #         prev.left = None
        #         prev.right = node
        #     if right:
        #         stack.append(right)
        #     if left:
        #         stack.append(left)
        #     prev = node


        # 
        curr = root

        while curr:
            if curr.left:
                predecessor = nxt = curr.left
                while predecessor.right:
                    predecessor = predecessor.right
                predecessor.right = curr.right
                curr.left = None
                curr.right = nxt
            curr = curr.right



# @lc code=end

