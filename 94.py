# binary tree middle order traverse
# let root to be r, left child to be lc and right child to be rc then
# middle order traverse is : lc if any , when return from lc then r and then rc
# use a recursive call
from typing import Optional, List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse_middle_order(self, root_of_b_tree: Optional[TreeNode]) -> List[int]:
        res = []
        if root_of_b_tree:
            res = self.traverse_middle_order(root_of_b_tree.left)
            res.append(root_of_b_tree.val)
            res = res + self.traverse_middle_order(root_of_b_tree.right)
        return res
