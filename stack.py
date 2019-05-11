#!python
from linkedlist import LinkedList # from folder.filename import Class

class Stack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        return True if self.list.size == 0 else False

    def length(self):
        """Return the number of items in this stack."""
        return self.list.size
    
    def push(self, item):
        """"Insert given item on top of stack
        Run time: O(1) because we only need to change head node"""
        self.list.prepend(item)
    
    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        head = self.list.head
        return None if head is None else head.data
    
    def pop(self):
        """Remove and return top item, if any, or raise ValueError if empty
        Run time: O(1) because we only need to change head node"""
        head = self.peek()
        self.list.delete(head)
        return head
