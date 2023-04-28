"""Creating a singly linked list."""

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insert_sll(self, value, position=None):
        """Default is to append node to end of list."""
        newNode = Node(value)
        if position == None:
            if self.head == None:
                self.head = newNode
                self.tail = newNode
            else:
                current_node = self.head
                while current_node.next != None:
                    current_node = current_node.next
                current_node.next = newNode
                self.tail = newNode
        elif position == 0:
            newNode.next = self.head
            self.head = newNode
        else:
            current_node = self.head
            current_pos = 0
            while current_pos < position - 1:
                current_pos += 1
                current_node = current_node.next
                if current_node == None:
                    raise ValueError("Position out of bounds.")
            newNode.next = current_node.next
            current_node.next = newNode

    def traverse_sll(self):
        if self.head is None:
            print("Head does not exist.")
        else:
            current_node = self.head
            while current_node != None:
                print(current_node.value)
                current_node = current_node.next


    def deleteNode(self, position=None):
        """Default is to delete last node."""
        if self.head is None:
            print("List does not exist.")
        else:
            if position == None:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    current_node = self.head
                    while True:
                        if current_node.next == self.tail:
                            break
                        current_node = current_node.next
                    current_node.next = None
                    self.tail = current_node        
            elif position == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            else:
                current_node = self.head
                current_pos = 0
                while current_pos < position:
                    prev_node = current_node
                    current_node = current_node.next
                    current_pos += 1
                prev_node.next = current_node.next
                current_node = None

    
    def deleteList(self):
        self.head = None
        self.tail = None


node1 = Node(1)
sll = SLinkedList()
sll.head = node1
sll.tail = node1

sll.insert_sll(2)
sll.insert_sll(3)
sll.insert_sll(4, 1)
sll.deleteNode(0)
print([node.value for node in sll])
