from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    max_depth = 0

    def dfs(self, root: Optional[TreeNode], current_depth: int):
        if root is not None:
            # print(root.val)
            current_depth += 1
            self.dfs(root.left, current_depth)
            self.dfs(root.right, current_depth)
        else:
            if current_depth > Solution.max_depth:
                Solution.max_depth = current_depth

    def get_max_depth(self, root: Optional[TreeNode]) -> int:
        self.dfs(root, 0)
        result = Solution.max_depth
        Solution.max_depth = 0
        return result


# test above dfs method
test = TreeNode(1)
test.right = TreeNode(2)

# generate a large tree of random to test above


s = Solution()
test_result = s.get_max_depth(test)
# 1 2 4 5 3 6 7
print(test_result)
# test above dfs method
