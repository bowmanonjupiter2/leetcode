from typing import List


class Solution:
    def safe_index(self, lst, value):
        try:
            return lst.index(value)
        except ValueError:
            return -1

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        result = []
        result_sorted = []
        has_zero = False

        if nums.count(0) >= 3:
            result.append((0, 0, 0))

        index_of_zero = self.safe_index(nums, 0)

        if index_of_zero != -1:
            has_zero = True
        else:
            nums.append(0)
            nums.sort()
            index_of_zero = self.safe_index(nums, 0)

        left_side = nums[:index_of_zero]
        right_side = nums[index_of_zero + 1:]

        for i_left, v_left in enumerate(left_side):
            for i_right, v_right in enumerate(right_side):
                if v_left + v_right > 0:
                    i_temp = self.safe_index(left_side, -(v_left + v_right))
                    if i_temp != -1 and i_temp != i_left:
                        result.append((v_left, -(v_left + v_right), v_right))
                elif v_left + v_right < 0:
                    i_temp = self.safe_index(right_side, -(v_left + v_right))
                    if i_temp != -1 and i_temp != i_right:
                        result.append((v_left, -(v_left + v_right), v_right))
        if has_zero:
            for left in left_side:
                if self.safe_index(right_side, -left) != -1:
                    result.append((left, -left, 0))

        for element in result:
            result_sorted.append(tuple(sorted(element)))

        return list(set(result_sorted))


s = Solution()
r = s.threeSum([-1, 0, 1, 2, -1, -4])
print(r)
