from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    nums3 = []
    idx_1 = 0
    idx_2 = 0
    while idx_1 <= m - 1 and idx_2 <= n - 1:
        if nums1[idx_1] <= nums2[idx_2]:
            nums3.append(nums1[idx_1])
            idx_1 += 1
        else:
            nums3.append(nums2[idx_2])
            idx_2 += 1

    while idx_1 <= m - 1:
        nums3.append(nums1[idx_1])
        idx_1 += 1
    while idx_2 <= n - 1:
        nums3.append(nums2[idx_2])
        idx_2 += 1

    for idx_3 in range(m+n):
        nums1[idx_3] = nums3[idx_3]


test_list_1 = [1, 2, 3, 0, 0, 0]
test_list_2 = [2, 5, 6]
merge(test_list_1, 3, test_list_2, 3)
print(test_list_1)
