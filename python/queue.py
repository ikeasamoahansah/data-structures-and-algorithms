class Node:
    
    def __init__(self, d):
        self.data = d
        self.next = None


class Queue:

    def __init__(self) -> None:
        self.head = Node
        self.tail = Node

    def peek(self):
        return self.head.data

    def enqueue(self, item):
        new_node = Node(item)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
            return self.tail.data
        self.head = self.tail = new_node

    def dequeue(self):
        if self.head:
            head = self.head
            self.head = head.next
            return head.data
        return None
