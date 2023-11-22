from typing import List
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        # 1st method(brutal force approach)
        # output = 0
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             # if nums[j]-nums[i] == diff and nums[k]-nums[j] == diff:
        #             #     output+=1
        #             if nums[j]-nums[i] == diff:
        #                 if nums[k]-nums[j] == diff:
        #                     output+=1
        #             else:
        #                 break
                    
        # return output
        # 2nd method:
        # Since we are looking for an arithmetic triplet, then we are sure about  these rules:
        # 3 consecutive numbers(a, b, c) are arithmetic triplet:
        # b-a == diff and c - b == diff
        # which means: b = diff + a , c = diff + b
        # which means: b= diff + a, c = diff + diff + a = 2*diff + a
        num_set = set(nums)
        output = 0
        for num in num_set:
            if num + diff in num_set and num + 2*diff in num_set:
                output+=1
        return output


        
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,
        18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,
        33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,
        48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,
        63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,
        78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,
        93,94,95,96,97,98,99,100,101,102,103,104,105,
        106,107,108,109,110,111,112,113,114,115,116,
        117,118,119,120,121,122,123,124,125,126,127,
        128,129,130,131,132,133,134,135,136,137,138,
        139,140,141,142,143,144,145,146,147,148,149,
        150,151,152,153,154,155,156,157,158,159,160,
        161,162,163,164,165,166,167,168,169,170,171,
        172,173,174,175,176,177,178,179,180,181,182,
        183,184,185,186,187,188,189,190,191,192,193,
        194,195,196,197,198,199,200]

# nums = [0,1,4,6,7,10]
diff = 3
ob = Solution()
print(ob.arithmeticTriplets(nums, diff))
