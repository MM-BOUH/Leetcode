from typing import Optional
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def isSymetricCheck(leftNode, rightNode):
            if leftNode is None and rightNode is None:
                return True
            if leftNode is None or rightNode is None:
                return False
            if leftNode.val != rightNode.val:
                return False
            return isSymetricCheck(leftNode.left, rightNode.right) and isSymetricCheck(leftNode.right, rightNode.left)
        if root is None:
            return True
        isSymetricCheck(root.left, root.right)
        