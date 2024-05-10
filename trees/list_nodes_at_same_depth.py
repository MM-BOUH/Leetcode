class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def add(self, val):
        new_node = TreeNode(val)
        if not self.root:
            self.root = new_node
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if not node.left:
                node.left = new_node
                break
            else:
                queue.append(node.left)
            if not node.right:
                node.right = new_node
                break
            else:
                queue.append(node.right)

if __name__ == "__main__":
    # Initialize the tree manually based on your description
    root = TreeNode(1)
    root.left = TreeNode(7, TreeNode(2), TreeNode(6, TreeNode(5), TreeNode(11)))
    root.right = TreeNode(9, None, TreeNode(9, TreeNode(5), None))

    tree = BinaryTree(root)

    # Function to perform in-order traversal to print the tree nodes for verification
    def in_order_traversal(node):
        if node:
            in_order_traversal(node.left)
            print(node.val, end=' ')
            in_order_traversal(node.right)
    def pre_order_traversal(node):
        if node:
            print(node.val, end=' ')
            pre_order_traversal(node.left)
            pre_order_traversal(node.right)
    def post_order_traversal(node):
        if node:
            post_order_traversal(node.left)
            post_order_traversal(node.right)
            print(node.val, end=' ')
    def breadth_first_search(node):
        queue = [node]
        if node:
            # while queue:
            #     print(queue.pop(0).val, end=' ')
            #     breadth_first_search(node.left)
            #     breadth_first_search(node.right)
            while queue:
                current = queue.pop(0)
                print(current.val, end=' ')
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
        
    

    
    in_order_traversal(tree.root)
    print("********DFS-the in_order traversal(left-root-right)")
    pre_order_traversal(tree.root)
    print("********DFS-the pre_order traversal(root-left-right)")
    post_order_traversal(tree.root)
    print("*******DFS-the post_order traversal(left-right-root)")
    breadth_first_search(tree.root)
    print("*******Breadth First Search")
    
