# class ListNode:
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            if head.next:
                new_head = head.next
                head.next = self.swapPairs(new_head.next)
                new_head.next = head
                return new_head
            else:
                return head
        else:
            return


node_1 = ListNode(1)
node_2 = ListNode(2)
node_3 = ListNode(3)
node_4 = ListNode(4)

node_1.next = node_2
node_2.next = node_3
# node_3.next = node_4

s = Solution()
result_head = s.swapPairs(node_1)

while result_head:
    print(result_head.val)
    result_head = result_head.next
