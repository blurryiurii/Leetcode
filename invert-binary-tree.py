# https://leetcode.com/problems/invert-binary-tree/
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# recursive (trivial)
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.left:
            root.left = self.invertTree(root.left)
        if root.right:
            root.right = self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root

# iterative (stack-based approach)
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return None
    if root.left:
        root.left = self.invertTree(root.left)
    if root.right:
        root.right = self.invertTree(root.right)
    root.left, root.right = root.right, root.left
    return root