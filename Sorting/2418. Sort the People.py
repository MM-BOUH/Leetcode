from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(heights)
        ## Bubble sort
        # for i in range(n):
        #     for j in range(i+1, len(heights)):
        #         if heights[i] < heights[j]:
        #             temp1 = heights[i]
        #             heights[i] = heights[j]
        #             heights[j] = temp1
        #             temp = names[i]
        #             names[i] = names[j]
        #             names[j] = temp
        
        #######Selection sorts
        # for i in range(n):
        #     max_idx = i
        #     for j in range(i + 1, n):
        #         if heights[j] > heights[max_idx]:
        #             max_idx = j
        #     heights[i], heights[max_idx] = heights[max_idx], heights[i]
        #     names[i], names[max_idx] = names[max_idx], names[i]
        
        
        ####Insertion sort
        for i in range(1, n):
            key_height = heights[i]
            key_name = names[i]
            j = i - 1
            while j >= 0 and key_height > heights[j]:
                heights[j + 1] = heights[j]
                names[j + 1] = names[j]
                j -= 1
            heights[j + 1] = key_height
            names[j + 1] = key_name
    


        return names        

sol = Solution()
names = ["Mary","John","Emma"]
heights = [180,165,170]
print(sol.sortPeople(names, heights))