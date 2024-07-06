# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sorted_array_to_bst(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            node = TreeNode(nums[0])
            return node
        else:
            middle = int(len(nums) / 2)
            node = TreeNode(nums[middle])
            node.left = self.sorted_array_to_bst(nums[0:middle])
            node.right = self.sorted_array_to_bst(nums[middle+1:len(nums)])
            return node


input_1 = [-10, -3, 0, 5, 9]
s = Solution()
result_tree = s.sorted_array_to_bst(input_1)


def in_order_traversal(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []
    # Traverse left subtree, process current node, and then traverse right subtree
    return in_order_traversal(root.left) + [root.val] + in_order_traversal(root.right)


result_walk_thru = in_order_traversal(result_tree)
print(result_walk_thru)
