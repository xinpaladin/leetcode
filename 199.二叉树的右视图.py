#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # if not root:
        #     return []
        # res = []
        # stack = [[root]]

        # while stack:
        #     layer_nodes = stack.pop()
        #     if not layer_nodes:
        #         break
        #     res.append(layer_nodes[-1].val)
        #     next_layer_nodes = []
        #     for node in layer_nodes:
        #         if node.left:
        #             next_layer_nodes.append(node.left)
        #         if node.right:
        #             next_layer_nodes.append(node.right)
        #     stack.append(next_layer_nodes)
        # return res

        from collections import deque
        if not root:
            return []
        stack, res = deque([root]), []
        while stack:
            l = len(stack)
            res.append(stack[-1].val)
            for _ in range(l):
                node = stack.popleft()
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        return res
# @lc code=end

