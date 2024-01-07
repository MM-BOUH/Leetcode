from typing import List
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        # digital logic and computing
        # 1. AND: This operation returns true if both operands are true. In binary terms, it returns 1 if both bits are 1.
        #        example: 2 and 3 will be 2. py: result = a & b 
        # 2. OR: This operation returns true if at least one of the operands is true. 
        # In binary terms, it returns 1 if either of the bits is 1.
        # example: 2 OR 3 results in 3. py: result = a | b
        # 3. XOR (Exclusive OR): This operation returns true only if one of the operands is true, but not both.
        #  In binary   terms,  it returns 1 if the bits are different.
        # EXAMPLE: 2 xor 3 results in 1. py: result = a ^ b
        # 4. NOT: This unary operation inverts the value of its operand. In binary terms, it turns 1 into 0 and 0 into 1.
        # The NOT operation doesn't work between two numbers like AND, OR, or XOR. py: result = ~a
        # 5. NAND (NOT AND): This is the inverse of AND. It returns true if both operands are not true. 
        # In binary terms, it returns 0 only if both bits are 1. py: result = ~(a & b)
        # 2 NAND 3 will be 1.
        # 6. NOR (NOT OR): This is the inverse of OR. It returns true only if both operands are false. 
        # In binary terms, it returns 1 only if both bits are 0. py: result = ~(a | b)
        # ex: the NOR operation of 2 and 3 results in 0
        # 7. XNOR (Exclusive NOR or Equivalence): This is the inverse of XOR.
        #  It returns true if both operands are equal (both true or both false). 
        # In binary terms, it returns 1 if the bits are the same.
        # ex:  2 XNOR 3 will be 0. py: result = ~(a ^ b)
        
        # encoded[i] = arr[i] XOR arr[i+1] => encoded[0] = arr[0] XOR arr[1] <=> arr[1] = encoded[0] xor arr[0]
        # there are multiple approaches to avoid list index out of range.
        # 
        # 1st approach:
        arr = [first]
        for i in range(len(encoded)):
            arr.append(encoded[i] ^ arr[i])
        return arr

