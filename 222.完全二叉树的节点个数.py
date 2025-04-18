#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # count = 0
        # def countChildNode(node, count):
        #     if not node:
        #         return count
        #     count += 1
        #     count = countChildNode(node.left, count)
        #     count = countChildNode(node.right, count)
        #     return count
        # count = countChildNode(root, count)
        # return count

        # if not root:
        #     return 0
        # left = self.countNodes(root.left)
        # right = self.countNodes(root.right)
        # return left + right + 1
        
        def check(num):
            node = root
            path = str(bin(num)).replace("0b",'')
            for i in path[1:]:
                if i == '0':
                    node = node.left
                elif i == '1':
                    node = node.right
                if not node:
                    return False
            return True
        
        if not root: return 0
        node = root
        depth = 0
        while node:
            depth += 1
            node = node.left
        if depth <= 1: return depth
        l = 1 << depth -1 
        r = l << 1 
        ans = l
        while l < r :
            mid = (l+r)//2
            if check(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid
        return ans

            
# @lc code=end

