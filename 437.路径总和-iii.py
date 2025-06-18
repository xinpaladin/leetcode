#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # 效率低 
        # def dfs(node, pre):
        #     nonlocal count
        #     if not node:
        #         return count
            
        #     for i in range(len(pre)):
        #         pre[i] += node.val
        #         if pre[i] == targetSum:
        #             count += 1
            
        #     if node.val == targetSum:
        #         count += 1
        #     pre.append(node.val)
        #     count = dfs(node.left, pre)
        #     count = dfs(node.right, pre)
        #     pre.pop()
        #     for i in range(len(pre)):
        #         pre[i] -= node.val
        #     return count
        # count = 0
        # pre = []
        # return dfs(root, pre)

        # 官方 深度优先搜索 时间复杂度O(n^2)
        # def rootSum(root, targetSum):
        #     if root is None:
        #         return 0

        #     ret = 0
        #     if root.val == targetSum:
        #         ret += 1

        #     ret += rootSum(root.left, targetSum - root.val)
        #     ret += rootSum(root.right, targetSum - root.val)
        #     return ret
        
        # if root is None:
        #     return 0
            
        # ret = rootSum(root, targetSum)
        # ret += self.pathSum(root.left, targetSum)
        # ret += self.pathSum(root.right, targetSum)
        # return ret

        # 前缀和
        prefix = collections.defaultdict(int)
        prefix[0] = 1

        def dfs(node, curr):
            if not node:
                return 0
            ret = 0
            curr += node.val
            ret += prefix[curr - targetSum]
            prefix[curr] += 1
            ret += dfs(node.left, curr)
            ret += dfs(node.right, curr)
            prefix[curr] -= 1
            return ret
        return dfs(root, 0)

# @lc code=end

