#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 递归
        # res = []

        # def dfs(node):
        #     if not node: return
        #     dfs(node.left)
        #     res.append(node.val)
        #     dfs(node.right)

        # dfs(root)
        # return res

        # 迭代 标记
        WHITE, GREY = 0, 1
        stack = [(WHITE, root)]
        res = []
        while stack:
            color, node = stack.pop()
            if not node: continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((GREY, node))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)

        return res


# @lc code=end

