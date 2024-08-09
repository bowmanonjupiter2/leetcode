from typing import List


class Solution:
    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        for idx, num in enumerate(numbers):
            remain = target - num
            if remain in numbers:
                idx_remain = numbers.index(remain)
                if idx_remain != -1 and idx_remain != idx:
                    return sorted([idx + 1, idx_remain + 1])
            else:
                continue
        return [-1]


s = Solution()
result = s.two_sum([5,25,75], 100)
print(result)
