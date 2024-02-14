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
        
    def removeNthFromEnd(self, n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = self.head
        start = dummy
        end = dummy

        # Move end ahead n + 1 times to create the gap
        for _ in range(n + 1):
            end = end.next

        # Move both pointers until end reaches the end of the list
        while end:
            start = start.next
            end = end.next

        # Remove the nth node from the end
        start.next = start.next.next

        self.head = dummy.next  # Update the head of the list

sol = Solution()
sol.append(1)
sol.append(2)
# sol.append(3)
# sol.append(4)
# sol.append(5)
sol.removeNthFromEnd(1)
sol.traverse()
    
    
    
### My approach, it will for some edge cases, but not for this -> head = [1,2,3] and n=1
### Need to use a different approach
"""""
            def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
                prev = None
                current = head
                while current:
                    next_node = current.next
                    current.next = prev
                    prev = current
                    current = next_node
                # print(prev)
                counter = 1
                current = prev
                modified_linked_list  = prev
                while current and current.next:
                    # print(current)
                    if counter == n-1:
                        current.next = current.next.next
                        modified_linked_list = current
                    counter+=1
                    current = current.next
                print("here is the modified linked list: ",modified_linked_list)
                prev = None
                current = modified_linked_list
                while current:
                    next_node = current.next
                    current.next = prev
                    prev = current
                    current = next_node
                return prev
        
    """