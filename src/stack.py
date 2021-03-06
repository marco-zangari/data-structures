"""Stack data structure."""
from linked_list import LinkedList


class Stack(object):
    """Stack object class."""

    def __init__(self, iterable=None):
        """Init new stack instance."""
        self._stck = LinkedList(iterable)

    def push(self, val):
        """Push new item on stack."""
        self._stck.push(val)

    def pop(self):
        """Pop last-in item on stack."""
        try:
            return self._stck.pop()
        except IndexError:
            raise IndexError('Cannot pop from an empty stack.')

    def __len__(self):
        """Return size of stack with len() function."""
        return len(self._stck)
