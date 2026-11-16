# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
from typing import Optional


class Solution:
    def mergeKLists(
        self, lists: list[Optional["ListNode"]]
    ) -> Optional["ListNode"]:
        heap = []

        # Include the first node of each non-empty list.
        for list_index, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, list_index, node))

        dummy = ListNode()
        tail = dummy

        while heap:
            _, list_index, node = heapq.heappop(heap)

            tail.next = node
            tail = node

            if node.next:
                heapq.heappush(heap, (node.next.val, list_index, node.next))

        tail.next = None
        return dummy.next