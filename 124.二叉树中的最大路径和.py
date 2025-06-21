#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float("-inf")

        def maxGain(node):
            nonlocal maxSum
            if not node:
                return 0
            left_max_gain = max(maxGain(node.left), 0)
            right_max_gain =max(maxGain(node.right), 0)

            tmp = node.val + left_max_gain + right_max_gain

            maxSum = max(maxSum, tmp)
            return node.val + max(left_max_gain, right_max_gain)
        maxGain(root)  
        return maxSum
# @lc code=end

