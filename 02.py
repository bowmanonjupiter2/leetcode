# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


# class ListNode:
#     def __init__(self, val=0, next_node=None):
#         self.val = val
#         self.next = next_node
# create two linked list according to above definition of ListNode
# list A
head_a = ListNode(2)
head_a.next = ListNode(4)
head_a.next.next = ListNode(3)
# list B
head_b = ListNode(5)
head_b.next = ListNode(6)
head_b.next.next = ListNode(4)


class Solution:
    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        result_head = None
        current = None

        while l1 and l2:
            current_sum = l1.val + l2.val + carry
            carry = current_sum // 10
            new_node = ListNode(current_sum - carry * 10)
            if not current:
                current = new_node
                result_head = current
            else:
                current.next = new_node
                current = new_node
            l1 = l1.next
            l2 = l2.next

        while l1:
            current_sum = l1.val + carry
            carry = current_sum // 10
            new_node = ListNode(current_sum - carry * 10)

            if not current:
                current = new_node
                result_head = current
            else:
                current.next = new_node
                current = new_node

            l1 = l1.next

        while l2:
            current_sum = l2.val + carry
            carry = current_sum // 10
            new_node = ListNode(current_sum - carry * 10)

            if not current:
                current = new_node
                result_head = current
            else:
                current.next = new_node
                current = new_node

            l2 = l2.next

        if carry > 0:
            new_node = ListNode(1)
            if not current:
                current = new_node
                result_head = current
            else:
                current.next = new_node
                current = new_node

        return result_head


s = Solution()
result = s.add_two_numbers(head_a, head_b)

while result:
    print(result.val)
    result = result.next
