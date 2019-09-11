# LinkedList

The problems in this section will singly linked list operations, doubly linked list operations,
linked list manipulation and conversions.

## Description

LinkedList is a data structure which consists of a `data` value and a `pointer` to another similar node. The first node of the linkied list
is known as `head`. The linked list imitates a chain structure where we can access the nodes only by traversing through the previous nodes starting from head.

Unlike arrays, the data elements are not stored in contiguous memory, but are linked using the pointer as mentioned above. Linkedlists are easy to extend or reduce. 

### Singly LinkedList

The above description constitutes of the singly linked list. For example, a diagramatic representation is given below.

### Doubly LinkedList

Each node in a Doubly linked list consists of an extra pointer know as the `previous` pointer. It points to the previous node.
The diagram below depicts a doubly linkedlist

### Circular LinkedList

A circular linkedlist is similar to singly linkedlist except the last node points towards head, forming a `circular` structure.
One of the advantages of circular linkedlist is starting from any node and traversing the entire list is possible.
Following is the graphical description of circular linkedlist:

## Representation

### Singly LinkedList

```
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None     # pointer to next node

```

### Doubly LinkedList

```
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None     # pointer to next node
        self.prev = None     # pointer to previous node

```

## General Complexities

Time complexity for various operations is given below:
- Insertion : <b>O(1)</b> , given that we know the location and have iterator to the location, otherwise O(n)
- Deletion : <b>O(1)</b> given that we know the location and have iterator to the location, otherwise O(n)
- Traversal / Search : <b>O(n)</b>

Space complexity is <b>O(n)</b> as we need to store all the nodes in some memory.