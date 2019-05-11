#!python
from linkedlist import LinkedList # from folder.filename import Class

class Queue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        return True if self.list.size == 0 else False

    def length(self):
        """Return the number of items in this queue."""
        return self.list.size

    def enqueue(self, item):
        """ Insert given item at back of queue
        Running time: O(1) since only need to change pointer to head"""
        self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        head = self.list.head
        return None if head is None else head.data
    
    def dequeue(self):
        """Remove and return item at front of queue or raise ValueError if queue empty
        Running time: O(1) since only need to change pointer to head"""
        head = self.front()
        if head == None:
            raise ValueError("list is empty")
        else:
            self.list.delete(head)
            return head
