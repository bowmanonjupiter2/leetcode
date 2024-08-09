from typing import List

sum_elements = lambda arr, idx: sum(map(lambda i: arr[i], idx))


class Solution:
    def find_median(self, nums1: List[int], nums2: List[int]) -> float:

        median_index_1 = []
        median_index_2 = []

        length_1 = len(nums1)
        if length_1 > 0:
            if length_1 % 2 == 0:
                median_index_1 = [(length_1 // 2) - 1, (length_1 // 2)]
            else:
                median_index_1 = [length_1 // 2]

        length_2 = len(nums2)
        if length_2 > 0:
            if length_2 % 2 == 0:
                median_index_2 = [(length_2 // 2) - 1, (length_2 // 2)]
            else:
                median_index_2 = [length_2 // 2]

        if len(median_index_1) == 0 and len(median_index_2) == 0:
            return 0.0

        if len(median_index_1) == 0:
            return sum_elements(nums2, median_index_2) / len(median_index_2)

        if len(median_index_2) == 0:
            return sum_elements(nums1, median_index_1) / len(median_index_1)

        if nums1[median_index_1[-1]] < nums2[median_index_2[0]]:
            return self.find_median(nums1[median_index_1[-1]: len(nums1)], nums2[0:median_index_2[0]])
        if nums2[median_index_2[-1]] < nums1[median_index_1[0]]:
            return self.find_median(nums1[0:median_index_1[0]], nums2[median_index_2[-1]: len(nums2)])

        temp = []
        for idx in median_index_1:
            temp.append(nums1[idx])
        for idx in median_index_2:
            temp.append(nums2[idx])

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
