class Stack:
    def __init__(self):
        self.stack = []
    def push(self, val):
        self.stack.append(val)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "the stack is empty"
    def is_empty(self):
        return len(self.stack) ==0
    def size(self):
        return len(self.stack)
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "the stack is empty"
class Solution:
    # def finalPrices(self, prices: List[int]) -> List[int]:
    #     stack = Stack()
    #     discounts = []
    #     for i in range(len(prices)):
    #         stack.push(prices[i])
    #         discount = False
    #         for j in range(i+1, len(prices)):
    #             if not stack.is_empty():
    #                 if stack.peek() < prices[j]:
    #                     continue
    #                 elif stack.pop() >= prices[j]:
    #                     discount = True
    #                     discounts.append(prices[i]-prices[j])
    #         if not discount:
    #             discounts.append(stack.pop())
    #     return discounts
    # CHATGPT METHOD
    def finalPrices(self, prices):
        # Stack to keep track of indices of prices for which discounts are to be found
        stack = []
        # Iterate through each price
        for i in range(len(prices)):
            # While stack is not empty and the current price is less than or equal to the price at the stack's top index
            while stack and prices[i] <= prices[stack[-1]]:
                # Apply discount to the price at the top index
                prices[stack[-1]] -= prices[i]
                # Pop since we've applied the discount for this price
                stack.pop()
            # Push the current index onto the stack
            stack.append(i)
        return prices

    