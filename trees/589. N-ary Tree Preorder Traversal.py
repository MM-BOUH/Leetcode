from typing import List
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def preorder(self, root:Node)-> List[int]:
        if root is None:
            return []
        output = []
        def traverse(node):
            output.append(node.val)
            if node.children:
                for child in node.children:
                    traverse(child)
        traverse(root)
        return output
if __name__ == "__main__":
    node5 = Node(5)
    node6 = Node(6)
    node3 = Node(3, [node5, node6])
    node2 = Node(2)
    node4 = Node(4)
    root = Node(1, [node3, node2, node4])
    
    sol = Solution()
    print(sol.preorder(root))  # Output should be [1, 3, 5, 6, 2, 4] 