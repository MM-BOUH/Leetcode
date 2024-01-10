# Node class to represent a node in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
        

# LinkedList class to represent the linked list
class LinkedList:
    def __init__(self):
        self.head = None
        
   # Method to insert a new node at the end of the linked list
    def append(self, data):
        new_node = Node(data)
        # if Linked list is empty(there is no head)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        print("Current: ", current)
        while current.next:
            print("current.next", current.next)
            current = current.next
        current.next = new_node # in python for example,
        # the next variabe is just another node(has data and next) that points to an 
        # object(another node), but in C, C++ a pointer is an address in the memory.
         # Conclusion of the append method in a singly linked list
         #in conclusion, at the first iteration we don't have a link between nodes,
         # after the second we'll tell the program that our first node points to the second node
         # and at the third iteration we'll tell our program that the second node points to the third one 
         # and finally the third node will points to null, and this is how we created a linked, where we know the first node(head) and the last node that points to null.
         
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
# linked_list.append(4)



   