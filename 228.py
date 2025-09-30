from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        result = []

        for idx, val in enumerate(nums):
            if idx == 0:
                prev = val
                start = 0
                continue
            else:
                if val - prev > 1:
                    left = nums[start:idx]
                    result.append([left[0], left[-1]])
                    start = idx
                prev = val
                continue

        left =  nums[start:idx+1]
        result.append([left[0], left[-1]])
        result_str = []
        for item in result:
            if item[0] == item[1]:
                result_str.append(str(item[0]))
            else:
                result_str.append(f"{item[0]}->{item[1]}")
        return result_str


s = Solution()
nums = [0, 1, 2, 4, 5, 7]
result = s.summaryRanges(nums)
print(result)
