"""Implement four traversal methods in bst."""


def bst_pre_order_traversal(tree):
    """Traverse a binary search tree with pre-order."""
    stack = []
    curr = tree.root
    while stack or curr:
        if node is curr:
            curr = stack.pop()
        else:
            yield curr.val
            stack.extend([curr.right, curr.left])
            curr = stack.pop()


def bst_post_order_traversal(self):
    """Traverse a binary search tree with post order."""
    stack = []
    curr = root
    while curr or stack:
        if curr:
            if curr.right:
                stack.append(curr.right)
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            if stack and (curr.right == stack):
                stack.pop()
                stack.append(curr)
                curr = curr.right
            else:
                yield curr.val
                curr = None


def bst_in_order_traversal(self):
    """Traverse a binary search tree with in order sequence."""
    stack = []
    curr = None
    while curr or stack:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            yield curr.val
            curr = curr.right


def bst_breadth_first_traversal(self):
    """Traverse binary search tree with breadth first sequence."""
    stack = []
    curr = root
    while stack or curr:
        if curr:
            yield curr
            stack.extend(curr.left, curr.right)
            curr = stack.pop(0)
        else:
            curr = stack.pop(0)


def bst_breadth_first_traversal(self):
    """Traverse a binary search tree via breadth first."""
    current = root
    nodes = []
    nodes.append(current)
    path = []
    while nodes:
        if current.left:
            left = current.left
            nodes.append(left)
        if current.right:
            right = current.right
            nodes.append(right)
        path.append(current)
        nodes.delete(current)
        current = nodes[0]
    yield path
