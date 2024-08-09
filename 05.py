class Solution:
    def longest_palindrome(self, s: str) -> str:

        if len(s) == 0:
            return s

        char_list = list(s)
        longest_palindrome = [char_list[0]]

        for idx in range(len(char_list) - 1):

            if char_list[idx] == char_list[idx + 1]:
                palindrome = []
                palindrome.insert(0, char_list[idx])
                palindrome.append(char_list[idx + 1])
                left = idx - 1
                right = idx + 2
                while left >= 0 and right < len(char_list):
                    if char_list[left] == char_list[right]:
                        palindrome.insert(0, char_list[left])
                        palindrome.append(char_list[right])
                        left -= 1
                        right += 1
                    else:
                        break
                if len(palindrome) > len(longest_palindrome):
                    longest_palindrome[:] = palindrome

            if idx > 0 and char_list[idx - 1] == char_list[idx + 1]:
                palindrome = []
                palindrome.append(char_list[idx])
                palindrome.insert(0, char_list[idx - 1])
                palindrome.append(char_list[idx + 1])

                left = idx - 2
                right = idx + 2
                while left >= 0 and right < len(char_list):
                    if char_list[left] == char_list[right]:
                        palindrome.insert(0, char_list[left])
                        palindrome.append(char_list[right])
                        left -= 1
                        right += 1
                    else:
                        break

                if len(palindrome) > len(longest_palindrome):
                    longest_palindrome[:] = palindrome

        return ''.join(longest_palindrome)


s = Solution()
print(s.longest_palindrome("aaaaa"))
