from typing import List


class Solution:
    def maximum_gap(self, nums: List[int]) -> int:

        maximum_gap = 0
        sorted_nums = sorted(nums)

        for i in range(0, len(sorted_nums) - 1):
            gap = sorted_nums[i + 1] - sorted_nums[i]
            if gap > maximum_gap:
                maximum_gap = gap

        return maximum_gap


s = Solution()
result = s.maximum_gap([3, 6, 9, 1])
print(result)
