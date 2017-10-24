"""Singly linked list data structure."""


class Node(object):
    """Make node object class."""

    def __init__(self):
        """Make node object class."""
        self.data = None
        self.next = None


class LinkedList(object):
    """Make linked list class."""

    def __init__(self):
        """Make linked list object."""
        self.head = None
        self.count = 0

    def push(self, val):
        """Push a new node on head of linked list."""
        new_node = Node()
        new_node.data = val
        new_node.next = self.head
        self.head = new_node
        self.count += 1
