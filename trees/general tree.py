class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        """ Adds a child node to this node. """
        self.children.append(child_node)

    def __repr__(self, level=0):
        """ Helper method to print the tree structure to the console. """
        ret = "\t" * level + repr(self.value) + "\n"
        for child in self.children:
            ret += child.__repr__(level+1)
        return ret

# Example usage
if __name__ == "__main__":
    root = TreeNode('Root')
    child1 = TreeNode('Child 1')
    child2 = TreeNode('Child 2')
    child1_1 = TreeNode('Child 1.1')
    child1_2 = TreeNode('Child 1.2')
    child2_1 = TreeNode('Child 2.1')

    # Build the tree
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(child1_1)
    child1.add_child(child1_2)
    child2.add_child(child2_1)

    # Print the tree structure
    print(root)
