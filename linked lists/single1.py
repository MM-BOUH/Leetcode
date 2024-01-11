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
        while current.next:
            current = current.next
        current.next = new_node 
        print("here is the new_node", new_node)
        print("Here is current.next", current.next)
        
        # in python for example,
        # the next variabe is just another node(has data and next) that points to an 
        # object(another node), but in C, C++ a pointer is an address in the memory.
         # Conclusion of the append method in a singly linked list
         #in conclusion, at the first iteration we don't have a link between nodes,
         # after the second we'll tell the program that our first node points to the second node
         # and at the third iteration we'll tell our program that the second node points to the third one 
         # and finally the third node will points to null, and this is how we created a linked, where we know the first node(head) and the last node that points to null.
         # زبدة الموضوع 
         # Yes, you've understood it correctly. In the context of linked lists, "adding a new node" is indeed about making the previous last node point to the new node. 
         # This might be a bit different from what you'd expect, especially if you're comparing it to adding items to an array or a list in a more traditional sense.
    
    def traverse(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
        
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.traverse()
# linked_list.append(4)



   