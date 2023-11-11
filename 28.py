def str_str(haystack: str, needle: str) -> int:
    if len(needle) == 0 or len(needle) > len(haystack):
        return -1

    list_matched_index_start = [i for i, ltr in enumerate(haystack) if ltr == needle[0]]

    if len(list_matched_index_start) == 0:
        return -1
    else:
        first_match_index = list_matched_index_start[0]

        for i in range(1, len(needle)):
            temp_match_index = -1
            found_this_one = False

            for jdx, j in enumerate(list_matched_index_start):
                if j != -1 and j + i < len(haystack) and needle[i] == haystack[j + i]:
                    found_this_one = True
                    if temp_match_index == -1:
                        temp_match_index = j
                else:
                    list_matched_index_start[jdx] = -1

            if not found_this_one:
                return -1
            else:
                first_match_index = temp_match_index

        return first_match_index


found = str_str("mississippi", "sipp")

if found == -1:
    print("not found")
else:
    print(found)
