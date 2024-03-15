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
'''brute force approach
def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
output = []
for i in range(len(nums1)):
found = False
for j in range(len(nums2)):
if nums1[i] == nums2[j]:
    if j == len(nums2)-1:
        output.append(-1)
        continue
    else:
        for k in range(j+1, len(nums2)):
            if nums2[k] > nums2[j]:
                output.append(nums2[k]) 
                found = True
                break
        if not found:
            output.append(-1)
return output
'''