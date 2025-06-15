#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 递归
        # def compare(left, right):
        #     if not left and not right:
        #         return True
            
        #     if not left or not right or (left.val != right.val) :
        #         return False

        #     return compare(left.left, right.right) and compare(left.right, right.left) 
        # return compare(root.left, root.right) 

        # 迭代
        if not root:
            return True
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            if not left and not right:
                continue
            
            if not left or not right or (left.val != right.val) :
                return False
            
            stack.append((left.right, right.left))
            stack.append((left.left, right.right))
            
        return True
# @lc code=end

