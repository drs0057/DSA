"""Creating a singly linked list."""

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


sll = SLinkedList()
node1 = Node(1)
node2 = Node(2)

sll.head = node1
sll.head.next = node2
sll.tail = node2