from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    ### My approach, it will for some edge cases, but not for this -> head = [1,2,3] and n=1
    ### Need to use a different approach
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