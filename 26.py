from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result = []
        for num in nums:
            if len(result) == 0:
                result.append(num)
            else:
                if num == result[-1]:
                    continue
                else:
                    result.append(num)
        for index, value in enumerate(result):
            nums[index] = value
        return len(result)


s = Solution()
test = s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
print(test)
