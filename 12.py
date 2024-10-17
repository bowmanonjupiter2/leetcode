import numpy as np


class Solution:
    search_array = np.array([["I", "V", "X"], ["X", "L", "C"], ["C", "D", "M"], ["M", "", ""]])

    def integer_to_roman(self, num: int) -> str:
        tmp_list = []
        result_list = []
        while num:
            remain = num % 10
            tmp_list.append(remain)
            num = (num - remain) / 10
        for idx, val in enumerate(tmp_list):
            if val == 4:
                result_list.append(self.search_array[idx, 1])
                result_list.append(self.search_array[idx, 0])
                continue
            if val == 9:
                result_list.append(self.search_array[idx, 2])
                result_list.append(self.search_array[idx, 0])
                continue
            if val < 5:
                i = 0
                while i < val:
                    result_list.append(self.search_array[idx, 0])
                    i += 1
                continue
            if val == 5:
                result_list.append(self.search_array[idx, 1])
            else:
                i = 0
                while i < val - 5:
                    result_list.append(self.search_array[idx, 0])
                    i += 1
                result_list.append(self.search_array[idx, 1])
        result_list.reverse()
        return ''.join(result_list)


s = Solution()
print(s.integer_to_roman(1994))
# if idx == 0:
#     if val == 4:
#         result_list.append("VI")
#         continue
#     if val == 9:
#         result_list.append("XI")
#     if val < 5:
#         i = 0
#         while i < val:
#             result_list.append("I")
#             i += 1
#         continue
#     if val == 5:
#         result_list.append("V")
#     else:
#         i = 0
#         while i < val - 5:
#             result_list.append("I")
#             i += 1
#         result_list.append("V")
# elif idx == 1:
#     if val == 4:
#         result_list.append("LX")
#         continue
#     if val == 9:
#         result_list.append("CX")
#     if val < 5:
#         i = 0
#         while i < val:
#             result_list.append("X")
#             i += 1
#         continue
#     if val == 5:
#         result_list.append("L")
#     else:
#         i = 0
#         while i < val - 5:
#             result_list.append("C")
#             i += 1
#         result_list.append("L")
# elif idx == 2:
#     if val == 4:
#         result_list.append("DC")
#         continue
#     if val == 9:
#         result_list.append("MC")
#     if val < 5:
#         i = 0
#         while i < val:
#             result_list.append("C")
#             i += 1
#         continue
#     if val == 5:
#         result_list.append("D")
#     else:
#         i = 0
#         while i < val - 5:
#             result_list.append("C")
#             i += 1
#         result_list.append("D")
# elif idx == 3:
#     while i < val:
#         result_list.append("M")
#         i += 1
