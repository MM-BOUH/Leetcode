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
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)

arr = [1,2,3]
print(arr)
print(linked_list)


   