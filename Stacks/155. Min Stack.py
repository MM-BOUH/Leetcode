# My solution
'''
# class MinStack:

#     def __init__(self):
#         self.stack = []

#     def push(self, val: int) -> None:
#         self.stack.append(val)

#     def pop(self) -> None:
#         if not self.is_empty():
#             return self.stack.pop()
#     def is_empty(self):
#         return self.stack == 0

#     def top(self) -> int:
#         if not self.is_empty():
#             return self.stack[-1]

#     def getMin(self) -> int:
#         print("Sorting the stack", self.stack.sort())
#         return min(self.stack)
'''
### CHATGPT SOLUTION
class Solution:
    def __init__(self):
        self.stack = []
        self.minStack = []
    
    def push(self, val):
        self.stack.append(val)
        
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)
    
    def pop(self):
        if not self.stack:
            return
        
        val = self.stack.pop()
        if val == self.minStack[-1]:
            self.minStack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]