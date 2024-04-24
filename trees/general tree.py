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
    def search(self, value):
        """ Search for a node with the specified value. """
        if self.value == value:
            return self
        for child in self.children:
            result = child.search(value)
            if result:
                return result
        return None
    
    def update(self, old_value, new_value):
        """ Update a node's value from old_value to new_value. """
        node = self.search(old_value)
        if node is not None:
            node.value = new_value
            return True
        return False
    
    def delete(self, value):
        """ Deletes a node with the specified value. """
        # Find the node and its parent
        parent, node = None, self
        stack = [(None, self)]
        while stack:
            parent, node = stack.pop()
            if node.value == value:
                break
            for child in node.children:
                stack.append((node, child))
        else:
            return False  # Value not found

        # Remove the node from its parent's children list
        if parent is None:
            raise Exception("Cannot delete the root node with this method")
        parent.children = [child for child in parent.children if child != node]
        return True
    
    
if __name__ == "__main__":
    root = TreeNode('Root')
    child1 = TreeNode('Child 1')
    child2 = TreeNode('Child 2')
    child1_1 = TreeNode('Child 1.1')
    child1_2 = TreeNode('Child 1.2')
    child1_3 = TreeNode('Child 1.2')
    child2_1 = TreeNode('Child 2.1')

    # Build the tree
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(child1_1)
    child1.add_child(child1_2)
    child1.add_child(child1_3)
    child2.add_child(child2_1)

    
    print("Searching for 'Child 1.2':", root.search('Child 1.2'))
    root.update('Child 1.1', 'Updated Child 1.1')
    print("After Updating 'Child 1.1' to 'Updated Child 1.1':")
    print(root)
    
