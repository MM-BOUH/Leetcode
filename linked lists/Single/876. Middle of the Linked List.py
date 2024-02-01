from typing import Optional
# solved
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self):
        self.head = None
    ### Append   
    def appendAtTheEnd(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    def appendAtTheBeginning(self, val):
       new_node = ListNode(val)
       if self.head:
           new_node.next = self.head
           self.head = new_node
    def appendAtASpecificPosition(self, val, desired):
        new_node = ListNode(val)
        if desired == 0:
            new_node.next = self.head
            self.head  = new_node
            return
        current = self.head
        counter = 0
        
        while current:
            if desired -1 == counter: # for the previous node
                print(f"desired: {desired} and counter {counter}")
                new_node.next = current.next
                current.next = new_node
                return 
            counter+=1
            current = current.next
        if desired > counter:
            print("the desired position is bigger than the length of the node")
    
    
    ## Traversing
    def traverse(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next
    def firstNode(self):
        print("The first node is: ", self.head.val)     
    def middleNode(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print("the middle node is : ",slow.val)
        return slow
    def lastNode(self):
        current = self.head
        while current:
            if current.next == None:
                print("the last node in this linked list is: ", current.val)
                return current
            current = current.next
    
           
linked_list = Solution()
linked_list.appendAtTheEnd(65)
linked_list.appendAtTheEnd(80)
linked_list.appendAtTheEnd(90)
linked_list.appendAtTheBeginning(1000)
linked_list.appendAtASpecificPosition(2000,9)
linked_list.traverse()
# linked_list.firstNode()
# linked_list.middleNode()
# linked_list.lastNode()

# head = [65,66,26,77,96,86,11,21,13,80]
# print(linked_list.middleNode(head))
 
'''
My solution won't work because this soltution is only for linked lists which have consecutive numbers
like [1,2,3,4,5]
class Solution:
    def length(self, head):
        current = head
        length=0
        while current:
            length+=1
            current = current.next
        return length

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = self.length(head)
        print("linked list, ", head)
        middle = length/2+1 if length%2==0 else length/2+1/2
        current = head
        linked_list = ListNode()
        while current:
            if current.val == middle:
                linked_list = current

            current = current.next  
        return linked_list
'''

    
