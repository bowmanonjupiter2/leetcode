class Solution:
    def compare_version(self, version1: str, version2: str) -> int:
        list_1 = version1.split('.')
        list_2 = version2.split('.')

        idx_1 = 0
        idx_2 = 0

        while idx_1 < len(list_1) and idx_2 < len(list_2):
            if int(list_1[idx_1]) < int(list_2[idx_2]):
                return -1
            elif int(list_1[idx_1]) > int(list_2[idx_2]):
                return 1
            else:
                idx_1 += 1
                idx_2 += 1

        while idx_1 < len(list_1):
            if int(list_1[idx_1]) > 0:
                return 1
            else:
                idx_1 += 1
        while idx_2 < len(list_2):
            if int(list_2[idx_2]) > 0:
                return -1
            else:
                idx_2 += 1

        return 0


s = Solution()
# result = s.compare_version("1.2", "1.10")
# result = s.compare_version("1.01", "1.001")
result = s.compare_version("1.0", "1.0.0.0")
if result == 1:
    print("version 1 is newer than version 2")
elif result == -1:
    print("version 1 is older than version 2")
else:
    print("version 1 is the same as version 2")
