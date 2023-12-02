from typing import List
class Solution:
    
    def convert_to_binary(self, num):
        if num == 0:
            return "0"
        binary = ""
        while num > 0:
            remainder = num % 2
            binary = str(remainder) + binary
            num = num // 2
        return binary

    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        binary_conversion = []
        for index in range(len(nums)):
            binary_conversion.append(self.convert_to_binary(index))
        
        output = 0
        
        ###Both approaches need to be optimized(especially for time complexity)
        # 1st approach
        for index in range(len(nums)):
            check_sum = 0
            for number in binary_conversion[index]:
                check_sum += int(number)
            if check_sum == k:
                output += nums[index]
        return output
    
        # 2nd approach: this approach will work until some testcases like this:
        #nums = [5,5,5]
        #k = 1, because, dictionaries don't accept redondance, they need unique keys
        # dictionary_correspondance = {}
        # for index in range(len(nums)):
        #     print(f"nums of index {index} is {nums[index]} and the binary conversion is {binary_conversion[index]}")
        #     dictionary_correspondance[nums[index]] = binary_conversion[index]
        # print("this is dictionary_correspondance: ", dictionary_correspondance)
        # for key, value in dictionary_correspondance.items():
        #     check_sum = 0
        #     for number in value:
        #         check_sum += int(number)
        #     if check_sum == k:
        #         output+=key
        # return output

obj = Solution()
# Didn't pass this testcase
nums = [5,5,5]
k = 1

# nums = [5,10,1,5,2]
# k = 1
print(obj.sumIndicesWithKSetBits(nums, k))

