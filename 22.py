from typing import List


class Solution:
    int_result = []
    parenthesis_result = []

    def is_valid(self, test_list: List) -> bool:
        sum = 0
        for i in test_list:
            sum += i
            if sum > 0:
                return False
        return True

    def try_add_parenthesis(self, work_list: List, left: List, right: List):
        if len(left) == 0 and len(right) == 0:
            self.int_result.append(work_list)
            return

        left_1 = left.copy()
        right_1 = right.copy()
        work_list_1 = work_list.copy()

        left_2 = left.copy()
        right_2 = right.copy()
        work_list_2 = work_list.copy()

        if len(left_1) > 0:
            work_list_1.append(left_1.pop())
            if self.is_valid(work_list_1):
                self.try_add_parenthesis(work_list_1, left_1, right_1)

        if len(right_2) > 0:
            work_list_2.append(right_2.pop())
            if self.is_valid(work_list_2):
                self.try_add_parenthesis(work_list_2, left_2, right_2)

    def generateParenthesis(self, n: int) -> List[str]:
        self.int_result = []
        self.parenthesis_result = []
        left = []
        right = []
        work = []

        for i in range(n):
            left.append(-1)
            right.append(1)

        self.try_add_parenthesis(work, left, right)

        for result in self.int_result:
            self.parenthesis_result.append(''.join(list(map(lambda x: '(' if x == -1 else ')', result))))

        return self.parenthesis_result


s = Solution()
r = s.generateParenthesis(1)
print(r)
