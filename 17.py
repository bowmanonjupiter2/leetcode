from typing import List
from itertools import product


class Solution:
    dial_char_dic = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    def flatmap(self, char_tuples):
        result = []
        for item in char_tuples:
            if isinstance(item, tuple):
                result.extend(self.flatmap(item))
            else:
                result.extend(item)
        return result

    def letterCombinations(self, digits: str) -> List[str]:
        product_result = []
        final_result = []
        for index, digit in enumerate(digits):
            if index == 0:
                product_result = self.dial_char_dic[digit]
            else:
                product_result = list(product(product_result, self.dial_char_dic[digit]))
        for element in product_result:
            flatten_list = self.flatmap(element)
            final_result.append(''.join(flatten_list))
        return final_result


solution = Solution()
test_result = solution.letterCombinations("5678")
print(test_result)
