#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from typing import Optional
# from treenode import list_to_tree, TreeNode
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # d = {}
        # def get_depth(node: Optional[TreeNode]):
        #     nonlocal res
        #     if not node:
        #         return 0
        #     if node in d:
        #         return d[node]
        #     left_depth = get_depth(node.left) + 1 if node.left else 0
        #     right_depth = get_depth(node.right) + 1 if node.right else 0
        #     res = max(left_depth + right_depth, res)
        #     depth = max(left_depth, right_depth)
        #     d[node]  = depth
        #     return depth

        # res = 0
        # get_depth(root)
        # # print(d)
        # return res
        self.ans = 1
        def depth(node):
            # 访问到空节点了，返回0
            if not node:
                return 0
            # 左儿子为根的子树的深度
            L = depth(node.left)
            # 右儿子为根的子树的深度
            R = depth(node.right)
            # 计算d_node即L+R+1 并更新ans
            self.ans = max(self.ans, L + R + 1)
            # 返回该节点为根的子树的深度
            return max(L, R) + 1

        depth(root)
        return self.ans - 1


# l = [1,2,3,4,5]
# root = list_to_tree(l)
# Solution().diameterOfBinaryTree(root)


# @lc code=end
