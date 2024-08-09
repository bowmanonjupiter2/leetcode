from typing import List


class Solution:
    def find_median(self, nums1: List[int], nums2: List[int]) -> float:
        temp = []
        temp.extend(nums1)
        temp.extend(nums2)
        temp.sort()

        length_temp = len(temp)
        if length_temp % 2 == 0:
            return (temp[(length_temp // 2) - 1] + temp[length_temp // 2]) / 2
        else:
            return temp[length_temp // 2]


s = Solution()
test_list_1 = [1, 2]
test_list_2 = [3, 4]
result = s.find_median(test_list_1, test_list_2)
print(result)
