from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        result = []
        for num in nums:
            if num != val:
                result.append(num)

        for index, val in enumerate(result):
            nums[index] = val

        return len(result)

