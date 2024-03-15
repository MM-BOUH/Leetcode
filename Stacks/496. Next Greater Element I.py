from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                top = stack.pop()
                next_greater[num] = top
            stack.append(num)
        for num in stack:
            next_greater[num] = -1
        result = [next_greater[num] for num in nums1]
        