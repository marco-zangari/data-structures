"""Test binary search tree."""

import pytest


@pytest.fixture
def empty_tree():
    """Empty tree, i.e. no node."""
    from bst import BST
    bst = BST()
    return bst


@pytest.fixture
def blncd_tree():
    """Build balanced tree fixture."""
    from bst import BST
    bst = BST()
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(15)
    bst.insert(25)
    bst.insert(35)
    bst.insert(45)
    bst.insert(70)
    bst.insert(60)
    bst.insert(90)
    bst.insert(55)
    bst.insert(65)
    bst.insert(80)
    bst.insert(100)
    return bst


@pytest.fixture
def unblncd_tree():
    """Build unbalanced tree fixture."""
    from bst import BST
    bst = BST()
    bst.insert(50)
    bst.insert(40)
    bst.insert(30)
    bst.insert(45)
    bst.insert(25)
    bst.insert(35)
    bst.insert(43)
    bst.insert(48)
    bst.insert(60)
    bst.insert(70)
    bst.insert(80)
    return bst

def test_init_isinstance_node(empty_tree):
    """Test node is node at initialization."""
    from bst import Node
    node = Node(50)
    assert isinstance(node, Node)