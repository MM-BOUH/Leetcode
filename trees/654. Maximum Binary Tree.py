from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        root = TreeNode()
        if not nums:
            return 
        largest = max(nums)
        root.val = largest
        root.left = self.constructMaximumBinaryTree(nums[0:nums.index(largest)])
        root.right = self.constructMaximumBinaryTree(nums[nums.index(largest)+1:])
        return root