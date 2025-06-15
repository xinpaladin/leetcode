#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # if not root:
        #     return []
        # stack = [[root]]
        # res = []

        # while stack:
        #     layer_nodes = stack.pop()
        #     if not layer_nodes:
        #         break
        #     layer_vals = []
        #     next_layer_nodes = []
        #     for node in layer_nodes:
        #         layer_vals.append(node.val)
        #         if node.left:
        #             next_layer_nodes.append(node.left)
        #         if node.right:
        #             next_layer_nodes.append(node.right)

        #     stack.append(next_layer_nodes)
        #     res.append(layer_vals)
        # return res

        if not root:
            return []
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)
        return res


# @lc code=end
