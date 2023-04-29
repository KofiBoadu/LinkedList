# LinkedList

This module contains two classes for implementing a singly linked list: Node and ListNode.

## Class: Node

The Node class represents a node in a singly linked list. It has the following attributes:

### value: The data stored in the node
### next: A reference to the next node in the list, defaulting to None

# Constructor


### def __init__(self, value):
Initializes a new node with the provided value.

# Class: ListNode

The ListNode class manages a singly linked list. It has the following attributes:

### head: A reference to the first node in the list, defaulting to None
#### Methods
#### add_first


### def add_first(self, value):
Adds a new node with the provided value to the beginning of the list.

### add_last


### def add_last(self, value):
#### Adds a new node with the provided value to the end of the list.

###nsize


### def size(self):
Returns the number of nodes in the list.

#### remove


### def remove(self, value):
Removes the first node with the provided value from the list. If the list is empty or the value is not found, it does nothing.

## reverse


### def reverse(self):
Reverses the order of nodes in the list and returns the new list.

## display


### def display(self):
Prints the list in a human-readable format.

## Example Usage


### my_list = ListNode()
### my_list.add_first(5)
### my_list.add_last(10)
### my_list.add_last(15)
### my_list.display()  ### Output: 5---->10---->15---->
### my_list.reverse()
### my_list.display()  ### Output: 15---->10---->5---->
