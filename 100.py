from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse_in_order(self, root_of_b_tree: Optional[TreeNode]) -> List[int]:
        res = []

        if not root_of_b_tree:
            res = ["null"]
        else:
            res = self.traverse_in_order(root_of_b_tree.left)
            res.append(root_of_b_tree.val)
            res = res + self.traverse_in_order(root_of_b_tree.right)

        return res

    def traverse_pre_order(self, root_of_b_tree: Optional[TreeNode]) -> List[int]:
        res = []

        if not root_of_b_tree:
            res = ["null"]
        else:
            res.append(root_of_b_tree.val)
            res = res + self.traverse_pre_order(root_of_b_tree.left)
            res = res + self.traverse_pre_order(root_of_b_tree.right)

        return res

    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        is_having_same_pre_order_sequence = self.traverse_pre_order(p) == self.traverse_pre_order(q)
        is_having_same_in_order_sequence = self.traverse_in_order(p) == self.traverse_in_order(q)
        if is_having_same_pre_order_sequence and is_having_same_in_order_sequence:
            return True
        else:
            return False
