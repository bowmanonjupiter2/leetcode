from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def get_target_node(self, head: Optional[ListNode], n: int) -> ListNode:
        target_pre = None
        target = curr = head

        temp_length = 1

        while curr:
            curr = curr.next
            temp_length += 1
            if curr and temp_length > n:
                target_pre = target
                target = target.next

        if not target_pre:
            return target.next
        else:
            target_pre.next = target.next
        return head


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

# link the nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

solution = Solution()
result_head = solution.get_target_node(node1, 5)

test_curr = result_head
while test_curr:
    print(test_curr.val)
    test_curr = test_curr.next
