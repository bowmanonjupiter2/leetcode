# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        new_head = curr_node = None

        while head1 and head2:
            if head1.val <= head2.val:
                temp_node = ListNode()
                temp_node.val = head1.val

                if curr_node:
                    curr_node.next = temp_node
                curr_node = temp_node

                head1 = head1.next
            else:
                temp_node = ListNode()
                temp_node.val = head2.val

                if curr_node:
                    curr_node.next = temp_node
                curr_node = temp_node

                head2 = head2.next

            if new_head is None:
                new_head = curr_node

        if curr_node is None:
            if head1:
                new_head = head1
            elif head2:
                new_head = head2
            else:
                new_head = None
        else:
            if head1:
                curr_node.next = head1
            elif head2:
                curr_node.next = head2
            else:
                curr_node.next = None

        return new_head


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)
node1.next = node2
node2.next = node3

node4 = ListNode(1)
node5 = ListNode(3)
node6 = ListNode(4)
node4.next = node5
node5.next = node6

node7 = ListNode(0)

s = Solution()
result = s.mergeTwoLists([], node7)
while result:
    print(result.val)
    result = result.next
