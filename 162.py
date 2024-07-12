import sys
from typing import List


class Solution:
    def find_peak_elements(self, nums: List[int]) -> int:
        peak_element_index = []
        temp_nums = [-sys.maxsize - 1]
        temp_nums.extend(nums)
        temp_nums.append(-sys.maxsize - 1)
        for i in range(0, len(temp_nums) - 2):
            if temp_nums[i] < temp_nums[i + 1] and temp_nums[i + 1] > temp_nums[i + 2]:
                peak_element_index.append(i)
        return peak_element_index[0]


s = Solution()
print(s.find_peak_elements([1, 2, 1, 5, 6, 4]))
