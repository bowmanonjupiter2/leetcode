class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        op_num = columnNumber
        while op_num > 26:
            if op_num % 26 == 0:
                col_char = 'Z'
                op_num -= 26
            else :
                col_char = chr(ord('A' )+ op_num % 26 - 1)

            result.append(col_char)

            op_num = op_num // 26
        result.append(chr(ord('A') + op_num - 1))
        return ''.join(reversed(result))


s = Solution()
output = s.convertToTitle(52)
print(output)
