from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        buff_list = []

        if not head:
            return

        while head and len(buff_list) < k:
            buff_list.append(head)
            head = head.next

        if len(buff_list) < k:
            return buff_list[0]
        else:
            i = 1
            while i <= k - 1:
                buff_list[-i].next = buff_list[-(i + 1)]
                i += 1
            buff_list[-k].next = self.reverseKGroup(head,k)
            return buff_list[-1]


node_1 = ListNode(1)
node_2 = ListNode(2)
node_3 = ListNode(3)
node_4 = ListNode(4)
node_5 = ListNode(5)

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5

s = Solution()
result = s.reverseKGroup(node_1, 3)
while result:
    print(result.val)
    result = result.next
