from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Assuming ListNode is defined elsewhere and the method is within a correct Pythonic class design.
# Here is a useful version of the `mergeTwoLists`:

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a prehead node that will help with the edge condition of an effectively empty new list.
        prehead = ListNode(0)

        # A current pointer that moves to actually sort the two.
        #This means that while changing prev.next, we are in fact changing the prehead
        # because the prev points to the prehead, and this is the beauty of linked lists
        prev = prehead
        
        while list1 and list2:
            # Navigate the 'sorted' ends and directly structurally sort.
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next
        
        # Handling of either remaining.
        prev.next = list1 if list1 else list2
        
        # `prehead.next` is now the head of our new 'merged' list.
        return prehead.next
