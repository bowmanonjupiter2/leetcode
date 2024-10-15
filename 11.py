from typing import List


class Solution:
    def max_area(self, banks: List[int]) -> int:
        max_v = 0
        if len(banks) <= 1:
            return 0
        if len(banks) == 2:
            max_v = min(banks)

        tuple_list = sorted((val, idx) for idx, val in enumerate(banks))

        for t in tuple_list:
            start_from = len(banks) - 1

            while start_from > t[1] and banks[start_from] < t[0]:
                start_from -= 1

            curr_v = t[0] * abs(start_from - t[1])
            if curr_v > max_v:
                max_v = curr_v

            start_from = 0

            while start_from < t[1] and banks[start_from] < t[0]:
                start_from += 1

            curr_v = t[0] * abs(t[1] - start_from)
            if curr_v > max_v:
                max_v = curr_v

            continue
        return max_v
