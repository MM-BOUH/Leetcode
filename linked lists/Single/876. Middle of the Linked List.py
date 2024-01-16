from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self):
        self.head = None
        
    def append(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    def traverse(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next
            
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
linked_list = Solution()
linked_list.append(65)
linked_list.traverse()
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

    
