
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, val):
        self.stack.append(val)
    def pop(self):
        if not self.stack:
            return
        return self.stack.pop()
    def peek(self):
        if not self.stack:
            return
        return self.stack[-1]
    def size(self):
        return len(self.stack)
    def is_empty(self):
        return len(self.stack)==0
    def sum_last_2(self):
        return int(self.stack[-1]) + int(self.stack[-2])

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = Stack()
        for op in operations:
            if re.match(r"^-?\d+$", op):
                stack.push(op)
            else:
                if op == "C":
                   stack.pop()
                elif op == "D":
                    stack.push(2*int(stack.peek()))
                elif op =="+":
                    stack.push(stack.sum_last_2())
        output = 0
        while not stack.is_empty():
            output += int(stack.pop())
        return output