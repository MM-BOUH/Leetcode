from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# First approach: this will return Time limit exceeded
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
        
    def isPalindrome(self) -> bool:
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print("the middle node is : " , slow)
        prev = None
        current = slow
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        left, right = self.head, prev
        while right: # this will start from the middle of the linked list and we will be sure that if there is no right, that left will be in the middle
            if right.val != left.val:
                return False
            right = right.next
            left = left.next
        self.head = prev
        return True


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(3)
linked_list.append(2)
linked_list.append(1)
print(linked_list.isPalindrome())
        