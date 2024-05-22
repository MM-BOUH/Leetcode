from typing import List
class Solution:
    def createTargetArray(slef, nums: List[int], index: List[int]) -> List[int]:
        #First approach using the built in function insert
        # target = []
        # for i in range(len(index)):
        #     target.insert(index[i], nums[i])
        # return target
        #Second Approach
        target = []
        for i in range(len(index)):
            target.append(None) # To make sure that there is enough space in the target
            for j in range(len(target)-1, index[i], -1): # We will use this to shift in case there are redundant indexes
                #by this target[j]=target[j-1], we will shift the target at j to the j-1, 
                # which on the right, because the loop is going backward
                target[j]=target[j-1]
                
            target[index[i]] = nums[i]
        return target
obj = Solution()
nums = [0,1,2,3,4]
index = [0,1,2,2,1]
print(obj.createTargetArray(nums, index))
