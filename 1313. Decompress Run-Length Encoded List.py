from typing import List
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        # splitting the array to number of pairs based on the length
        # using a generator expression
        pairs = ((nums[i], nums[i + 1]) for i in range(0, len(nums), 2))
        # Using a list comprehension
        # pairs = [(nums[i], nums[i + 1]) for i in range(0, len(nums), 2)]
        print(pairs)
         # here: it'll print: <generator object Solution.decompressRLElist.<locals>.<genexpr> at  0x7fb9a53b4400>
        output = []
        for pair in pairs:
            freq = pair[0]
            val = pair[1]
            print(f"freq:{freq} and value is {val}")
            for i in range(0, freq):
                output.append(val)
        print(output)
        return output