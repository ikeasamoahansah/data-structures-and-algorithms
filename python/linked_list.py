# class Node:

#     def __init__(self, item):
#         self.item = item
#         self.next = None


# class LinkedList:

#     def __init__(self):
#         self.head = None

#     # Insert at beginning
#     def insert_at_start(self, new_data):
#         new_node = Node(new_data)
#         new_node.next = self.head
#         self.head = new_node

#     # Insert after a node
#     def insert_after(self, prev_node, new_data):

#         if prev_node is None:
#             print("The given previous node must be in the linked list")
#             return
        
#         new_node = Node(new_data)
#         new_node.next = prev_node.next
#         prev_node.next = new_node


#     # Insert at the end
#     def insert_at_end(self, new_data):
#         new_node = Node(new_data)

#         if self.head is None:
#             self.head = new_node
#             return

#         last = self.head
#         while last.next:
#             last = last.next
        
#         last.next = new_node


#     # Deleting a Node
#     def delete_node(self, position):
#         if self.head is None:
#             return
        
#         temp = self.head

#         if position == 0:
#             self.head = temp.next
#             temp = None
#             return
        
#         # Find key to be deleted
#         for i in range(position - 1):
#             temp = temp.next
#             if temp is None:
#                 break

        
#         # If key not present
#         if temp is None:
#             return
        
#         if temp.next is None:
#             return
        
#         next_node = temp.next.next
#         temp.next = None
#         temp.next = next_node

    
#     # Searching for an element
#     def search_linked_list(self, key):
        
#         current = self.head

#         while current is not None:
#             if current.item == key:
#                 return True
            
#             current = current.next

#         return False
    

#     # Sort linked list

#     def sort_linked_list(self, head):

#         current = head
#         index = Node(None)

#         if head is None:
#             return
#         else:
#             while current is not None:
#                 index = current.next

#                 while index is not None:
#                     if current.item > index.item:
#                         current.item, index.item = index.item, current.item
                    
#                     index = index.next
#                 current = current.next


#     # Print the linked list
#     def printList(self):
#         temp = self.head
#         while (temp):
#             print(str(temp.item) + " ", end="")
#             temp = temp.next


# if __name__ == '__main__':

#     llist = LinkedList()
#     llist.insert_at_end(1)
#     llist.insert_at_start(2)
#     llist.insert_at_start(3)
#     llist.insert_at_end(4)
#     llist.insert_after(llist.head.next, 5)

#     print('linked list:')
#     llist.printList()

#     print("\nAfter deleting an element:")
#     llist.delete_node(3)
#     llist.printList()

#     print()
#     item_to_find = 3
#     if llist.search_linked_list(item_to_find):
#         print(str(item_to_find) + " is found")
#     else:
#         print(str(item_to_find) + " is not found")

#     llist.sort_linked_list(llist.head)
#     print("Sorted List: ")
#     llist.printList()



class Node:
    
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = Node | None


    # Traversing

    def traverse(self):
        current = self.head

        while current:
            print(current.val)
            current = current.next

    # Delete

    def delete_node(self, index):
        if self.head == None:
            return None
        
        if index == 0:
            new_head = self.head.next
            self.head.next = None
            return new_head
        
        current = self.head
        prev = None
        count = 0

        while count < index and current:
            prev = current
            current = current.next
            count += 1

        if current is not None:
            prev.next = current.next
            current.next = None
        else:
            print("Invalid index")
        return self.head


llist = LinkedList()
llist.head = Node(6)
llist.head.next = Node(5)
llist.head.next.next = Node(3)
llist.traverse()
llist.delete_node(1)
