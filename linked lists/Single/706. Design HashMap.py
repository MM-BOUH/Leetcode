class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
class MyHashMap:
    def __init__(self):
        self.head = None
    def put(self, key: int, value: int) -> None:
        current = self.head
        while current:
            if current.key == key:
                print(f"there is a key already and it's {key} let's modify it")
                current.val = value
                print(f"it's updated with {value} and the the current map is: {current}")
                return
            current = current.next 
        new_node = Node(key, value)
        new_node.next = self.head
        self.head = new_node
        print(f"Put: {key} -> {value}")
        return
    def get(self, key: int) -> int:
        print(f"I was called to check whether the key: {key} exists")
        current = self.head
        while current:
            if current.key == key:
                print(f"the key {key} exists and its value is {current.val}")
                return current.val
            current = current.next
        print(f"the key {key} does not exist and I will return -1")
        return -1

    def remove(self, key: int) -> None:
        current = self.head
        prev = None
        while current:
            if current.key ==  key:
                if prev:
                    print(f"I was called to remove {current.key} and {current.val}")
                    #When you modify the prev.next pointer in the remove method to point to current.next, you're effectively updating the linked list's structure in place. 
                    #This change persists even after the remove method completes because you're modifying the actual connections between the nodes in the linked list.
                    prev.next= current.next
                else:
                    self.head = current.next
                return
            prev = current
            current = current.next




# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)