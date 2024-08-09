


class Solution:
    def zip_loop_part(self, input: str) -> str:
        result_list = input.split('.')
        if len(result_list) <= 1:
            return input
        else:
            remaining = result_list[1]
            

    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
         quotient = numerator / denominator
         quotient_str = quotient.__str__()
