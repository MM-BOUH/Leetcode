from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self, val):
        self.container.append(val)
    
      
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

    def insert_characters(self, s):
        for c in s:
            self.push(c)
    def reverse(self):
        print(f"size {stack.size()}")    
        for _ in range(stack.size()):
            print(self.pop(), end='')
        print("")
    ## another way of reversing
    def reverse_string(self):
        reversed_string = ""
        while not self.is_empty:
            reversed_string += self.pop()
        return reversed_string
        
stack = Stack()
s = "Hello world"
stack.insert_characters(s)
stack.reverse()
stack.reverse_string()
