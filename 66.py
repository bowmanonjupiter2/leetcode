from typing import List


def plus_one(digits: List[int]) -> List[int]:

    i = len(digits) - 1

    while i >= 0:
        if digits[i] + 1 < 10:
            digits[i] = digits[i] + 1
            return digits
        else:
            digits[i] = digits[i] + 1 - 10
            i -= 1

    if i == -1:
        digits.insert(0, 1)
        return digits
    # list_length = len(digits)
    # list_sum = 0
    # for index, value in enumerate(digits):
    #     list_sum += value * 10 ** (list_length - index - 1)
    # list_sum += 1
    # result_list = []
    # result_length = list_length
    # if (list_sum // 10 ** result_length) > 0:
    #     result_length += 1
    #
    # print(list_sum)
    # print(result_length)
    #
    # while result_length > 0:
    #     result_length -= 1
    #     result_list.insert(0, list_sum % 10 ** result_length)
    #
    # return result_list


print(plus_one([1, 2, 3]))
