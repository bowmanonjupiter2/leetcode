from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insert_sort_work_list(self, work_list: List[ListNode], work_node: ListNode):
        if len(work_list) == 0:
            work_list.append(work_node)
            return
        else:
            left = 0
            right = len(work_list)
            target_index = left + (right - left) // 2
            while True:
                if work_node.val <= work_list[target_index].val:
                    right = target_index
                else:
                    left = target_index

                target_index = left + (right - left) // 2

                if target_index == left:
                    if work_node.val >= work_list[left].val:
                        target_index = right
                    else:
                        target_index = left
                    break

                continue
            work_list.insert(target_index, work_node)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        result_head = result_tail = None
        work_list: List[ListNode] = []
        for curr_node in lists:
            if curr_node:
                self.insert_sort_work_list(work_list, curr_node)

        while len(work_list) > 0:
            smallest = work_list.pop(0)
            if not result_head:
                result_head = result_tail = smallest
            else:
                result_tail.next = smallest
                result_tail = smallest

            next_one = smallest.next
            if next_one:
                self.insert_sort_work_list(work_list, next_one)

        return result_head


test_node_1 = ListNode(-1)
test_node_2 = ListNode(1)

test_node_1.next = test_node_2


test_node_3 = ListNode(-3)
test_node_4 = ListNode(1)
test_node_5 = ListNode(4)

test_node_3.next = test_node_4
test_node_4.next = test_node_5

test_node_6 = ListNode(-2)
test_node_7 = ListNode(-1)
test_node_8 = ListNode(0)
test_node_9 = ListNode(2)

test_node_6.next = test_node_7
test_node_7.next = test_node_8
test_node_8.next = test_node_9

test_list = [test_node_1, test_node_3, test_node_6]

s = Solution()
test_result = s.mergeKLists(test_list)

while test_result:
    print(test_result.val)
    test_result = test_result.next
