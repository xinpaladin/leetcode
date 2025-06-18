#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 递归
        # if not preorder or not inorder:
        #     return None
        # root = TreeNode(preorder[0])

        # if len(preorder) == 1:
        #     return root

        # index = inorder.index(preorder[0])

        # left_preorder = preorder[1 : index + 1]
        # right_preorder = preorder[index + 1 :]
        # left_inorder = inorder[:index]
        # right_inorder = inorder[index + 1 :]

        # left_node = self.buildTree(left_preorder, left_inorder)
        # right_node = self.buildTree(right_preorder, right_inorder)
        # root.left = left_node
        # root.right = right_node
        # return root

        # 另一种递归

        def myBuildTree(
            preorder_left: int,
            preorder_right: int,
            inorder_left: int,
            inorder_right: int,
        ):
            if preorder_left > preorder_right:
                return None
            root_index = preorder_left
            inorder_root = index[preorder[root_index]]
            root = TreeNode(preorder[root_index])

            left_size = inorder_root - inorder_left
            root.left = myBuildTree(
                preorder_left + 1,
                preorder_left + left_size,
                inorder_left,
                inorder_root - 1,
            )
            root.right = myBuildTree(
                preorder_left + 1 + left_size,
                preorder_right,
                inorder_root + 1,
                inorder_right,
            )
            return root

        n = len(preorder)
        # 构造哈希映射，帮助我们快速定位根节点
        index = {element: i for i, element in enumerate(inorder)}
        return myBuildTree(0, n - 1, 0, n - 1)


# @lc code=end
