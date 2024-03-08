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
    ### My approach will not check for the nested parantheses
'''
        def is_balanced(self, s):
            for c in s:
                if c == "(" or c == ")" or c =="{" or c=="}" or c=="[" or c=="]":
                    self.push(c)
            possible_parantheses = ""
            while not self.is_empty():
                possible_parantheses += self.pop()
            print("possible parantheses: ", possible_parantheses)
            left = 0
            right = len(possible_parantheses) - 1
            while left<right:
                
                # if (possible_parantheses[left] == ")" and possible_parantheses[right] == "(")  or \
                # (possible_parantheses[left] == "}" and possible_parantheses[right] == "{") or \
                # (possible_parantheses[left] == "]" and possible_parantheses[right] == "["):
                #     print("Hello")
                #     return True
                if (possible_parantheses[left] == ")" and possible_parantheses[right] == "(") :
                    return True
                elif (possible_parantheses[left] == "}" and possible_parantheses[right] == "{"):
                    return True
                elif (possible_parantheses[left] == "]" and possible_parantheses[right] == "["):
                    print("Hello")
                    return True
                left +=1
                right -=1
                
            return False 
    '''
def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2


def is_balanced(s):
    stack = Stack()
    for ch in s:
        if ch=='(' or ch=='{' or ch == '[':
            stack.push(ch)
        if ch==')' or ch=='}' or ch == ']':
            if stack.size()==0:
                return False
            if not is_match(ch,stack.pop()):
                return False
    print(stack.size())
    return stack.size()==0
    

if __name__ == '__main__':
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))