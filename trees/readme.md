# Study of Tree Data Structures

## Introduction
This section provides an overview of tree data structures, an essential concept in computer science used for representing hierarchical data. Starting with trees is beneficial before delving into more complex structures like graphs due to their structured and simpler nature.

## Key Topics

### Types of Trees
Various trees serve different purposes, mainly in optimizing data access and manipulation:
- **General Trees**: a node can have any number of children, from zero (making it a leaf node) to many (more than two).
- **Binary Trees**: Each node has up to two children.
- **Binary Search Trees (BST)**: Organizes data in a manner where each node contains a key greater than all keys in its left subtree and less than those in its right subtree.
- **Balanced Trees** (e.g., AVL Trees, Red-Black Trees): Ensures the tree remains balanced for optimal data access performance.

 
### Advanced Tree Structures
For more complex scenarios, advanced trees can be used:
- **Segment Trees**: Efficiently answer range queries and update operations on array intervals.
- **Fenwick Trees (Binary Indexed Trees)**: Provides a way to represent an array of numbers for cumulative frequency tables or prefix sum arrays.

### Tree Traversal
#### Depth First Search (DFS) in Trees

Depth First Search (DFS) is a traversal approach that can be applied to both trees and graphs. In the context of trees, DFS explores as deep into one branch of the tree as possible before retracting to explore other branches. There are three common DFS methods used in tree traversal:

##### In-order Traversal
- **Method**: Visit left subtree, root, right subtree.
- **Usage**: Often used for binary search trees where this method retrieves data in a sorted order.

##### Pre-order Traversal
- **Method**: Visit root, left subtree, right subtree.
- **Usage**: Useful for operations like copying the tree, where you need to encounter nodes before their descendants.

##### Post-order Traversal
- **Method**: Visit left subtree, right subtree, root.
- **Usage**: Ideal for operations like safely deleting nodes, as it processes children before their corresponding parent nodes.

Each traversal method serves different purposes and can be chosen based on the specific requirements of the operation you need to perform on the tree.
![Tree Traversal Methods](https://media.geeksforgeeks.org/wp-content/uploads/20230623123129/traversal.png "Tree Traversal Methods")



## Applications
Trees are widely used in many applications such as database management, file systems, rendering scenes in computer graphics, and more. Their ability to represent and manage hierarchical data makes them indispensable in advanced algorithms and systems.
1. **N-ary Tree Preorder Traversal** (LeetCode ID: 589) - **Easy**
   - [N-ary Tree Preorder Traversal](https://leetcode.com/problems/n-ary-tree-preorder-traversal/)

2. **Maximum Depth of Binary Tree** (LeetCode ID: 104) - **Easy**
   - [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

3. **Symmetric Tree** (LeetCode ID: 101) - **Easy**
   - [Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)

4. **Invert Binary Tree** (LeetCode ID: 226) - **Easy**
   - [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)

5. **Search in a Binary Search Tree** (LeetCode ID: 700) - **Easy**
   - [Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/)
6. **Maximum Binary Tree** (LeetCode ID: 654) - **Medium**
   - [Maximum Binary Tree](https://leetcode.com/problems/maximum-binary-tree/description/)
7. **Validate Binary Search Tree** (LeetCode ID: 98) - **Medium**
   - [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)


## Conclusion
In summary, the landscape of tree data structures encompasses various types of trees, each with its unique characteristics and applications. Binary trees are a fundamental type of tree where each node can have up to two children. When a node has no children, it is referred to as a leaf. Binary search trees (BSTs) are a specialized form of binary trees that maintain a specific order, where the left child of a node contains a value less than its parent, and the right child contains a value greater than its parent. This property makes BSTs exceptionally useful for operations like search, insert, and delete.

Traversal of trees is another critical concept and can be accomplished via Depth First Search (DFS) or Breadth First Search (BFS). DFS includes three primary methods: In-order traversal, which visits nodes in a left-root-right pattern; Pre-order traversal, which visits nodes in a root-left-right pattern; and Post-order traversal, which visits nodes in a left-right-root pattern. These methods allow us to explore the depths of a tree as deeply as possible before backtracking.

On the other hand, BFS, also known as Level Order traversal, follows a different principle. It utilizes the concept of a queue to visit nodes level by level, starting from the root. Each node is visited and its children are enqueued in a FIFO manner. This process continues iteratively until all nodes are visited and the queue is empty.

Understanding these structures and traversal methods is paramount for anyone delving into data structures and algorithms, as they provide a foundation for representing and managing hierarchical data efficiently in various computing tasks.

