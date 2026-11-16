class MyLinkedList:

    def __init__(self):
        self.val = 0
        self.next = self
        self.prev = self
        self.size = 0

    def _get_node(self, index: int):
        """Return the node at index, or None if the index is invalid."""
        if index < 0 or index >= self.size:
            return None

        # Start from the closer end of the list.
        if index < self.size // 2:
            node = self.next
            for _ in range(index):
                node = node.next
        else:
            node = self.prev
            for _ in range(self.size - 1, index, -1):
                node = node.prev

        return node

    def get(self, index: int) -> int:
        node = self._get_node(index)
        return node.val if node else -1

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            index = 0
        if index > self.size:
            return

        # Find the node that will follow the new node.
        if index == self.size:
            following = self
        else:
            following = self._get_node(index)

        new_node = ListNode(val)
        previous = following.prev

        new_node.prev = previous
        new_node.next = following
        previous.next = new_node
        following.prev = new_node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        node = self._get_node(index)
        if node is None:
            return

        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1


class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None
        self.prev = None