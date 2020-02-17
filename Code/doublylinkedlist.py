

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = None

    def __len__(self):
        return self.size

    def append(self, item):
        node = Node(item)
        if not self.tail:
            self.head = node
