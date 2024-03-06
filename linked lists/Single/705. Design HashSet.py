class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashSet:
    def __init__(self):
        self.head = None
    
    ## To add to the hashset
    def add(self, key):
        if not self.contains(key):
            new_node = Node(key)
            new_node.next = self.head
            self.head = new_node
            return
    def remoove(self, key):
        current = self.head
        prev = None
        
        while current:
            if current.val == key:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return
            prev = current
            current = current.next
            
            
    def contains(self, key):
        current = self.head
        while current:
            if current.val == key:
                return True
            current = current.next
        return False
# Your MyHashSet object will be instantiated and called as such:
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
obj = MyHashSet()
print(obj.add(1))
print(obj.add(2))
print(obj.contains(1))
print(obj.contains(3))
print(obj.add(2))
print(obj.contains(2))
print(obj.remoove(2))
print(obj.contains(2))

        
        