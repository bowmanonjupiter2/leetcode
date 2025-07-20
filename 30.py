from typing import List


class Solution:
    def find_sub_string(self, s: str, words: List[str]) -> List[int]:
        # Create a list to store word information
        word_info = []
        result = []
        
        # For each word, find all its occurrences in the string
        for word in words:
            word_length = len(word)
            occurrences = []
            
            # Find all occurrences of the word in the string
            start = 0
            while True:
                index = s.find(word, start)
                if index == -1:  # Word not found
                    break
                occurrences.append(index)
                start = index + 1
            
            # Create sublist with word length as first element, followed by occurrence indices
            word_data = [word_length] + occurrences

            if len(word_data) == 1:
                return result
            
            word_info.append(word_data)

        for tmp_list in word_info:
            for element in tmp_list[1:]:
                try:
                    self.recursive_search(element,word_info)
                except Exception as e:
                    continue
            result.append(element)
        
        return result
    def recursive_search(self, target_index: int, lst: list[list[int]]):
        for i, sublist in enumerate(lst):
            for idx in sublist[1:]:
                if idx == target_index:
                    if len(lst)==1:
                        return
                    else:
                        new_target = target_index + sublist[0]
                        new_lst = lst[:i] + lst[i+1:]
                        return self.recursive_search(new_target, new_lst)
        raise Exception(f"Target index {target_index} not found in any sublist.")

if __name__ == "__main__":
    s = "barfoothefoobarman"
    words = ["foo","bar"]
    result = Solution().find_sub_string(s, words)
    print(result)



