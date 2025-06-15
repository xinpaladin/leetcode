from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




def list_to_tree(nums) -> Optional[TreeNode]:
    if not nums:
        return None
    
    root = TreeNode(nums[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(nums):
        node = queue.popleft()
        
        if nums[i] is not None:
            node.left = TreeNode(nums[i])
            queue.append(node.left)
        i += 1
        
        if i < len(nums) and nums[i] is not None:
            node.right = TreeNode(nums[i])
            queue.append(node.right)
        i += 1
    
    return root

def tree_to_list(root) -> Optional[List]:
    if not root:
        return []
    
    queue = deque([root])
    result = []
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # 去除末尾多余的None
    while result[-1] is None:
        result.pop()
    
    return result


# 使用示例
# nums = [3,9,20,None,None,15,7]
# root = list_to_tree(nums)
# print(tree_to_list(root))  
