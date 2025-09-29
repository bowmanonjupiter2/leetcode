# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_num_of_nodes = self.countNodes(root.left)
        right_num_of_nodes = self.countNodes(root.right)
        return left_num_of_nodes + right_num_of_nodes + 1
