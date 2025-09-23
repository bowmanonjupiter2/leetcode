class Solution:

    def check_and_return_quotient(self, quotient: int):
        if quotient > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif quotient < -(2 ** 31):
            return -2 ** 31
        else:
            return quotient

    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0

        if divisor == 1:
            return self.check_and_return_quotient(dividend)

        if divisor == -1:
            return self.check_and_return_quotient(-dividend)

        result_sign_indicator = 1

        if (dividend > 0 > divisor) or (dividend < 0 < divisor):
            result_sign_indicator = -1

        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)
        quotient = 0
        remain = abs_dividend

        sum_of_abs_divisor = abs_divisor
        sum_of_steps = 1

        while remain >= sum_of_abs_divisor:
            remain = remain - sum_of_abs_divisor

            quotient += sum_of_steps

            sum_of_abs_divisor += abs_divisor
            sum_of_steps += 1

        while remain >= abs_divisor:
            remain = remain - abs_divisor
            quotient += 1

        if result_sign_indicator > 0:
            return self.check_and_return_quotient(quotient)
        else:
            return self.check_and_return_quotient(-quotient)


s = Solution()
test_result = s.divide(2147483647, 2)
print(test_result)
