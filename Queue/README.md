# Queues

This section will cover problems on queue creation, manipulation, conversion and circular queues

## Description

A queue is data structure to store data elements. However, unlike array, the elements can be inserted (enqueue) or removed(dequeue) in a particular order.
The order is generally a FIFO (First in First Out)

Following is the graphical representation of queue.


A queue can be implemented using an array or linkedlist.

### Circular Queue

A circular queue is similar to a queue, except the last or rear of the queue is connected to the start. We can also say that a circular queue is
`fixed-sized queue`

### Priority Queue

Every element of the queue is assigned a priority. Hence, an element with higher priority is dequeued before the element with lower priority


## Queue Operations

- enqueue :  insert element to the queue.
- dequeue : remove element from the queue.
- rear : it is the end of the queue.
- front : it is the starting element of the queue.

## General Complexities

The time complexity for all the above queue operations is <b>O(1)</b> and the space complexity
is <b>O(n)</b> where n is length of the stack.

The time complexity of search operation is <b>O(n)</b>
