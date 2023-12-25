from typing import List
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ############################# First approach and it needs to be optimized
        # For the left sum
        leftSum, rightSum = [], []
        currentleftSum = 0
        ### For the leftSum
        # The leftSum can be efficiently calculated in a single pass through the 
        # list by accumulating the sum as you go.
        # This works because each new element in leftSum is just the sum of all the numbers
        # to the left of the current  index, which you've already seen.
        for i in range(len(nums)):
          if i == 0:
              leftSum.append(0)
          else:
              currentleftSum += nums[i-1]
              leftSum.append(currentleftSum)
        ### For the right sum
        ### You're right that when you're at a certain position in the list, 
        #you haven't yet "seen" the elements to the right, so you can't just 
        # accumulate them in a single pass like you did with the leftSum. this results in a time complexity of O(n²)
        #  calculate the rightSum in a single pass from the end of the list to the beginning
        # This is not the most optimized approach, I still can optimize by you calculating
        # the rightSum in a single pass from the end of the list to the beginning
        for i in range(len(nums)):
            if i == len(nums)-1:
                rightSum.append(0)
            else:
                currentRightSum = 0
                for j in range(i+1, len(nums)):
                    currentRightSum+=nums[j]
                rightSum.append(currentRightSum)
        output = []
        for k in range(len(nums)):
            output.append(abs(leftSum[k]-rightSum[k]))
        
        return output