# Trees

The problems in this module will cover tree traversals, binary trees, binary search trees and construction and conversions of the trees.

## Description

A tree is a data structure which imitates the function of a physical tree to store data. The data structure starts with a `root` node which stores data and pointer to a group of nodes which are 
called as `children`. The individual `child` node can act as an independent node with its own children. The connection between the node and its children is known as `branch`.
A tree node with no children is known as `leaf` node.

Following is an illustration of an n children tree. 

![alt Tree Structure](https://www.tutorialspoint.com/data_structures_algorithms/images/binary_tree.jpg)
ref: [image link](https://www.tutorialspoint.com/data_structures_algorithms/images/binary_tree.jpg)

## General Complexity

Worst case Time and Space complexity for a general tree traversal is <b>O(n)</b> since you need to traverse all the nodes.
Insert and Delete operation can also take O(n) time and space.

There are different types of trees, which can have varying time and space complexities.

## Types of trees

Trees can be divided into following types

1. Binary Tree
2. Binary Search Tree
3. AVL or Height Balanced Tree
4. Red Black Tree
5. B-Tree

## Representation

A tree node can be represented as a python class with following attributes

```
class TreeNode:
    def __init__(data):
        self.data = data    # stored data value
        self.children = []  # Array represnting pointers to the children node
```



