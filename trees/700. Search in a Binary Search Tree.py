from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None
        #It means that the function will call itself again and again until there is no val < root.val in the first case, or no val > root.val   in the second case. then it will pass to the third condition if root.val == val: it will return the node with its subnodes if this condition is true.
        if val < root.val:
            return self.searchBST(root.left, val)
        if val > root.val:
            return self.searchBST(root.right, val)
        if root.val == val:
            return root
