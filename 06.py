class Solution:
    def convert(self, s: str, num_of_rows: int) -> str:

        if num_of_rows == 1:
            return s

        char_list = list(s)
        result_list = []

        for row in range(num_of_rows):
            idx = 0
            n = 0
            while True:
                idx = n * (num_of_rows - 1) + row
                if idx < len(char_list):
                    result_list.append(char_list[idx])
                    # print(char_list[idx], end="\t")
                else:
                    break
                n += 2
                if row != 0 and row != num_of_rows - 1:
                    idx = n * (num_of_rows - 1) - row
                    if idx < len(char_list):
                        result_list.append(char_list[idx])
                        # print(char_list[idx], end="\t")
                    else:
                        break
            # print()
        return "".join(result_list)


s = Solution()
result = s.convert("ABCDEFGHIJK", 2)
print(result)
