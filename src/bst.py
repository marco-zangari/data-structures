"""Implement binary search tree methods.

Hat tip: http://www.laurentluce.com/posts/binary-search-tree-library-in-python/
AND: Magnus Lie Hetlund Algorithms: Mastering Basic Algorithms in the Python/
Language
."""


class Node(object):
    """Node for binary search tree data structure."""

    def __init__(self, val, parent=None):
        """Initialize node for binary search tree."""
        self.left = None
        self.right = None
        self.parent = parent
        self.val = val


class BST(object):
    """Create binary search tree data structure."""

    def __init__(self, iterable=None):
        """Initiatalize the BST."""
        self.root = None
        self.depth = 0
        self._size = 0
        if iterable:
            if isinstance(iterable, (list, tuple, set)):
                for item in iterable:
                    self.insert.item
                else:
                    raise TypeError('Iterable must be list, tuple, or set')

    def insert(self, val):
        """Insert node into binary search tree."""
        if self.root:
            curr = self.root
            while True:
                if val > curr.val:
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = Node(val, curr)
                        self._size += 1
                        return
                if val < curr.val:
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = Node(val, curr)
                        self._size += 1
                        return
                if val == curr.val:
                    return
        else:
            self.root = Node(val)
            self._size += 1
            return

    def search(self, val):
        """."""
        if self.root is None:
            raise KeyError
        else:
            curr = self.root
            while True:
                if val > curr.val:
                    if curr.right:
                        curr = curr.right
                    else:
                        raise ValueError('No such value in tree')
                elif val < curr.val:
                    if curr.left:
                        curr = curr.left
                    else:
                        raise ValueError('No such value in tree')
                elif val == curr.val:
                    return curr

    def size(self):
        """Return the size of BST."""
        return self._size

    def depth(self):
        """Return depth of BST."""

    def _contains_(self, val):
        """Return whether node or not."""
        try:
            self.search(val)
        except KeyError:
            return False
        return True

    def balance(self):
        """Balance node returns int, positive or negative."""

    def delete(self, val):
        """Delete node from binary search tree."""
        curr = self.search(val)  # curr = node to delete
        parent = curr.parent

        if not curr.left and not curr.right:  # node has no children
            if curr.val < parent.val:
                parent.left = None
            if curr.val > parent.val:
                parent.right = None
            if curr == self.root:
                self.root = None
                return

        if not curr.right:  # node has one child
            if curr.val < parent.val:
                parent.left = curr.left
                curr.left.parent = curr.parent

        if not curr.left:  # node has one child
            if curr.val > parent.val:
                parent.right = curr.right
                curr.right.parent = curr.parent

        if curr == self.root:
            if not curr.right:
                self.root = curr.left
                return

        if curr.left and curr.right:  # node has two children
            target = curr.left
            while target:
                if target.right:
                    target = target.right
                else:
                    break
            if curr.left.parent == curr:  # if the node is one away
                target.parent = curr.parent
                target.right = curr.right
                target.right.parent = target
            if curr.parent:
                if curr.parent.val > curr.val:
                    curr.parent.left = target
                if curr.parent.val < curr.val:
                    curr.parent.right = target
                else:
                    self.root = target

            elif target.left:  # target node has one child
                target.parent.right = target.left
                target.left.parent = target.parent
                target.right = curr.right
                target.left = curr.left
                target.parent = curr.parent
                target.right.parent = target
                target.left.parent = target
            else:
                target.parent = None  # target node has no children
                target.parent = curr.parent
                target.left = curr.left
                target.right = curr.right

    def bst_pre_order_traversal(self):
        """Traverse a binary search tree with pre-order."""
        if self.root is None:
            raise ValueError('The tree has no nodes.')
        stack = []
        curr = self.root
        while stack or curr:
            if curr:
                yield curr.val
                if curr.right:
                    stack.append(curr.right)
                curr = curr.left
            else:
                curr = stack.pop()

    def bst_post_order_traversal(self):
        """Traverse a binary search tree with post order."""
        if self.root is None:
            raise ValueError('The tree has no nodes.')
        stack = []
        curr = self.root
        while curr or stack:
            if curr:
                if curr.right:
                    stack.append(curr.right)
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                if stack and (curr.right == stack[-1]):
                    stack.pop()
                    stack.append(curr)
                    curr = curr.right
                else:
                    yield curr.val
                    curr = None

    def bst_in_order_traversal(self):
        """Traverse a binary search tree with in order sequence."""
        if self.root is None:
            raise ValueError('The tree has no nodes.')
        stack = []
        curr = self.root
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                yield curr.val
                curr = curr.right

    def bst_breadth_first_traversal(self):
        """Traverse a binary search tree via breadth first."""
        if self.root is None:
            raise ValueError('The tree has no nodes.')
        curr = self.root
        nodes = []
        nodes.append(curr)
        while nodes:
            curr = nodes.pop(0)
            if curr.left:
                left = curr.left
                nodes.append(left)
            if curr.right:
                right = curr.right
                nodes.append(right)
            yield curr.val
