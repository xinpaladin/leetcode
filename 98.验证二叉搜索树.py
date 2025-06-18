#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 递归解法 
        # def helper(node, lower=float("-inf"), upper=float("inf")) -> bool:
        #     if not node:
        #         return True
        #     val = node.val
        #     if val <= lower or val >= upper:
        #         return False
        #     if not helper(node.left, lower, val):
        #         return False
        #     if not helper(node.right, val, upper):
        #         return False
        #     return True

        # return helper(root)

        # 迭代解法 中序遍历
        stack, inorder = [], float('-inf')
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if cur.val <= inorder:
                return False
            inorder = cur.val
            cur = cur.right
        return True

# @lc code=end
