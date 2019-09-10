# Binary Trees

Trees with only `two` children are known as binary trees. The two children are know as the left and right child node respectively.

Binary trees can be divided further into 4 types:
- <b>Full Binary Tree</b>: This is a tree which has 2 or 0 children. No node in this tree has a single child.
- <b>Complete Binary Tree</b>: All the levels in this tree are completely filled i.e have two children except maybe the last level
- <b>Perfect Binary Tree</b>: All the levels in this tree are completely filled, including the last level.
- <b>Skewed Binary Tree</b>: A skewed binary tree is completely dominated by either of its children. Here dominated means having large number of nodes one one side as compared to another.
- <b>Balanced Binary Tree</b>: The difference between the left and right subtree is always less than equal to one for every node in a balanced binary tree.


## Representation

A binary tree has only two children, hence it can be represented as follows:

```
class Node:
    def __init__(self, data):
        self.data = data   # data to store
        self.left = None   # pointer to left subtree
        self.right = None  # pointer to right subtree

```

## General Complexities

The worst case time and space complexity for a general binary tree is <b>O(n)</b> as all nodes need to be traversed for any
operation.

# Binary Search Trees (BST)

BST is a special type of binary tree which satisfies the conditions below for each node:

- the left subtree has nodes with values less than the current node.
- the right subtree has nodes with values greater than the current node.

You can perform operations like search , insert and delete on BST. It is represented similar to binary tree.

## BST Complexities

The worst case complexity of a BST is <b>O(n)</b> , whereas the best case complexity is <b>O(h)</b> where h is the height of the tree.

## AVL Tree
 
AVL is a type of BST which is a height balanced tree. Due to this property, the time complexity for all the
operations is <b>O(log<sub>2</sub>n)</b>.

The space complexity however is <b>O(n)</b>


