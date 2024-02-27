from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # The 2 pointers should not start at the same position.
        # Fast should be one step ahead from the beginning otherwise the condition will be true(if fast == slow)
        if not head:
            return False
        fast = head.next
        slow = head
        while fast and fast.next:
            
            if fast.next == None:
                return False
            if fast == slow:
                return True
            slow = slow.next
            fast = fast.next.next