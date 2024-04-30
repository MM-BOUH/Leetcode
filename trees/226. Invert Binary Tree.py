# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        
        # Swap the left and right children of the current node
        root.left, root.right = root.right, root.left
        
        # Recursively invert the left and right subtree
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

    # My firs approach: it's correct, but is using a list to store the inverted tree, which is not correct. the output should be a tree as well.
    # def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     output = []
    #     if root is None:
    #         return []
    #     output.append(root.val)
    #     def invert(node):
    #         if node is None:
    #             return 
    #         invert_right, invert_left = node.left, node.right
    #         if invert_left:
    #             output.append(invert_left.val)
    #         if invert_right:
    #             output.append(invert_right.val)
    #         invert(invert_left)
    #         invert(invert_right)
        
    #     invert(root)
    #     print(output)
    #     return output


        