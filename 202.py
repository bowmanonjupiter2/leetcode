class Solution:

    def __init__(self):
        self.trail = set()

    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        new_num = 0
        curr_num = n
        while curr_num > 0:
            remainder = curr_num % 10
            new_num += remainder * remainder
            curr_num = (curr_num - remainder) // 10

        if new_num == n:
            return False
        else:
            if new_num in self.trail:
                return False
            else:
                self.trail.add(new_num)
                return self.isHappy(new_num)


s = Solution()
if s.isHappy(2):
    print("Happy")
else:
    print("unhappy")
