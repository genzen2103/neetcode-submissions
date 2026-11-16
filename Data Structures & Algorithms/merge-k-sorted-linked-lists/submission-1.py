from typing import Optional


class Solution:
    def mergeKLists(
        self, lists: list[Optional["ListNode"]]
    ) -> Optional["ListNode"]:

        def merge_two(
            a: Optional["ListNode"],
            b: Optional["ListNode"],
        ) -> Optional["ListNode"]:
            dummy = ListNode()
            tail = dummy

            while a and b:
                if a.val <= b.val:
                    tail.next = a
                    a = a.next
                else:
                    tail.next = b
                    b = b.next
                tail = tail.next

            tail.next = a if a else b
            return dummy.next

        if not lists:
            return None

        # Merge neighboring pairs, then merge those results in later rounds.
        while len(lists) > 1:
            merged_lists = []

            for i in range(0, len(lists), 2):
                a = lists[i]
                b = lists[i + 1] if i + 1 < len(lists) else None
                merged_lists.append(merge_two(a, b))

            lists = merged_lists

        return lists[0]