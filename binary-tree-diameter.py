# https://leetcode.com/problems/diameter-of-binary-tree/

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS (could also be done iteratively with stack)
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)


            res = max(res, left + right)
            return 1 + max(left, right)
        
        dfs(root)

        return res