# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def get_intersection_node(self, head_a: ListNode, head_b: ListNode) -> Optional[ListNode]:

        intersection_node = None
        stack_a = []
        stack_b = []
        while head_a:
            stack_a.append(head_a)
            head_a = head_a.next
        while head_b:
            stack_b.append(head_b)
            head_b = head_b.next

        while len(stack_a) > 0 and len(stack_b) > 0:
            temp_a = stack_a.pop()
            temp_b = stack_b.pop()
            if temp_a is temp_b:
                intersection_node = temp_a
            else:
                break

        return intersection_node


# s = Solution()
#
# # create this list using list A [4,1,8,4,5] and list B [5,6,1,8,4,5] these two list intersect at node value is 8
# # generate two lists to test above
# # list A
# head_a = ListNode(4)
# head_a.next = ListNode(1)
# node_8 = ListNode(8)
# head_a.next.next = node_8
# node_4 = ListNode(4)
# head_a.next.next.next = node_4
# node_5 = ListNode(5)
# head_a.next.next.next.next = node_5
#
# head_b = ListNode(5)
# head_b.next = ListNode(6)
# head_b.next.next = ListNode(1)
# head_b.next.next.next = node_8
# head_b.next.next.next.next = node_4
# head_b.next.next.next.next.next = node_5
#
# intersection_result_node = s.get_intersection_node(head_a, head_b)
# print(intersection_result_node.val)



