# Definition for a binary tree node.

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    depths = set()

    def pre_order_traverse(self, root: Optional[TreeNode], current_depth: int):
        if root is not None:
            current_depth += 1
            if root.left is not None:
                self.pre_order_traverse(root.left, current_depth)
            elif root.right is not None:
                self.pre_order_traverse(root.right, current_depth)
            else:
                Solution.depths.add(current_depth)

    def is_balanced(self, root: Optional[TreeNode]) -> bool:
        Solution.depth_list = set()
        self.pre_order_traverse(root, 0)
        return len(Solution.depths) <= 2


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.left.left.left = TreeNode(8)

s = Solution()
if s.is_balanced(root):
    print("balanced binary tree")
else:
    print("not a balanced binary tree")
