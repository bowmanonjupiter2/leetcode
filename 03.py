class Solution:
    def longest_sub_string(self, s: str) -> int:
        longest = 0
        window = []
        for char in s:
            if char in window:
                if len(window) > longest:
                    longest = len(window)

                start = window.index(char) + 1
                end = len(window)
                if start < end:
                    window = window[start: end]
                else:
                    window = []

            window.append(char)

        if len(window) > longest:
            longest = len(window)

        return longest


s = Solution()
result = s.longest_sub_string("dvdf")
print(result)
