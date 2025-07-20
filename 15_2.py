from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        try:
            index_of_zero = nums.index(0)
        except ValueError:
            index_of_zero = -1

        left_cursor = 0
        left_end = left_cursor
        right_cursor = len(nums) - 1
        right_end = right_cursor

        while nums[left_end] < 0 and left_end <= len(nums):
            left_end += 1
        left_end -= 1
        while nums[right_end] > 0 and right_end >= 0:
            right_end -= 1
        right_end += 1

        if left_end == right_end:
            return result

        while left_cursor <= left_end and right_cursor >= right_end:
            if index_of_zero != -1 and nums[left_cursor] + nums[right_cursor] == 0:
                result.append([nums[left_cursor], 0, nums[right_cursor]])
                left_cursor += 1
                right_cursor -= 1
                continue
            else:
                is_found = False
                temp = nums[left_cursor] + nums[right_cursor]
                if temp < 0:
                    i = right_end
                    while i < right_cursor:
                        if nums[i] == -temp:
                            result.append([nums[left_cursor], nums[i], nums[right_cursor]])
                            left_cursor += 1
                            right_cursor -= 1
                            is_found = True
                            break
                        i += 1
                    if not is_found:
                        left_cursor += 1
                    continue
                else:
                    j = left_end
                    while j > left_cursor:
                        if nums[j] == -temp:
                            result.append([nums[left_cursor], nums[j], nums[right_cursor]])
                            left_cursor += 1
                            right_cursor -= 1
                            is_found = True
                            break
                        j -= 1
                    if not is_found:
                        right_cursor -= 1
                    continue

        if right_end - left_end > 3:
            result.append([0, 0, 0])

        return result


s = Solution()
r = s.threeSum([-2, 0, 1, 0])
print(r)
