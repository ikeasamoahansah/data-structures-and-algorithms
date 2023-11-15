class Node:
    
    def __init__(self, d):
        self.data = d
        self.prev = None


class Stack:
    def __init__(self):
        self.head = Node

    def peek(self):
        return self.head.data
    
    def push(self, item):
        new_node = Node(d=item)
        if self.head:
            new_node.prev = self.head
            self.head = new_node
            return self.head.data
        self.head = new_node

    def pop(self):
        if self.head:
            head = self.head
            self.head = head.prev
            return head.data
        return None