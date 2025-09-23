class Solution:
    def reverseBits(self, n: int) -> int:
        bin_str = format(n,'032b')
        list_bin = list(bin_str)
        list_bin.reverse()
        str_bin = ''.join(list_bin)
        int_str = int(str_bin,2)
        return int_str


s = Solution()
result = s.reverseBits(43261596)
print(result)