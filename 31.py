from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) <= 1:
            return
        is_found = False
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                temp = nums[i]
                nums[i] = nums[i - 1]
                nums[i - 1] = temp
                is_found = True
                break

        if not is_found:
            nums.sort()
        else:
            return


s = Solution()
test_input = [3, 1, 2]
s.nextPermutation(test_input)
print(test_input)
