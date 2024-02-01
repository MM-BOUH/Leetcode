from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = ListNode(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        
    def reverseList(self) -> Optional[ListNode]:
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        # print("the reversed linked list is :", prev.val)
        # self.head = prev, because we don't want to pass the head as an argument. 
        # Now, we have the reversed linked list in the head variable, and now we can print it easily using the printList
        self.head = prev
        return prev

    def printList(self):
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original List:")
linked_list.printList()

linked_list.reverseList()

print("Reversed List:")
linked_list.printList()