from typing import List


class Solution:

    def recursive_search_in_remaining_words(self, s: str, words: List) -> bool:
        for word in words:
            if s.startswith(word):
                clone_words = words.copy()
                clone_words.remove(word)
                if len(clone_words) == 0:
                    return True
                else:
                    remain_string = s[len(word): len(s)]
                    if len(remain_string) < len(clone_words[0]):
                        return False
                    else:
                        return self.recursive_search_in_remaining_words(remain_string, clone_words)
        return False

    def find_all_indices(self, target: str, sub: str) -> List[int]:
        indices = []
        start = 0
        while start < len(target):
            start = target.find(sub, start)
            if start == -1:
                break
            indices.append(start)
            start += 1  # Move past the last found substring
        return indices

    # def merge_the_same_words(self, words: List[str]) -> List[str]:
    #     if len(words) == 0:
    #         return []
    #     curr_str = words[0]
    #
    #     pass

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        result = []

        if len(set(words)) == 1:
            words = ["".join(words)]

        for word in words:
            word_indexes = self.find_all_indices(s, word)
            if len(word_indexes) == 0:
                continue
            else:
                clone_words = words.copy()
                clone_words.remove(word)
                if len(clone_words) == 0:
                    result.extend(word_indexes)
                    return result

                for word_index in word_indexes:
                    remain_string = s[word_index + len(word): len(s)]
                    if len(remain_string) < len(clone_words[0]):
                        continue
                    else:
                        if self.recursive_search_in_remaining_words(remain_string, clone_words):
                            result.append(word_index)

        return sorted(list(set(result)))


s = Solution()
result = s.findSubstring("aaaaaaaaaaaaaaaa", ["a", "a", "a"])
print(result)
