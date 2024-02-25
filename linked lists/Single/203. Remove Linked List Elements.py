from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self) -> None:
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
        
    def traverse(self):
        current = self.head
        
        while current:
            print(current.val)
            current = current.next
        
    def removeElements(self, val: int):
        dummy = ListNode(next=self.head)
        current = dummy
        
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
                
            else:
                current = current.next
        return dummy.next

sol = Solution()
# sol.append(7)      
# sol.append(7)      
# sol.append(7)      
# sol.append(7)      
sol.append(1)      
sol.append(2)      
sol.append(6)      
sol.append(3)      
sol.append(4)      
sol.append(5)      
sol.append(6)   
print("Before removing")   
sol.traverse()
print("After removing") 
print(sol.removeElements(val=6))  
sol.traverse()