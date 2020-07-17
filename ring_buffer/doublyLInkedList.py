class ListNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self, node=None):
        self.node = node
        self.head = None
        self.tail = None
        self.length = 1 if not node else 0
