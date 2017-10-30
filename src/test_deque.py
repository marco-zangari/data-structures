"""Test script for deque module."""


def test_deque_object_type():
    """Test instance of type has type deque."""
    from deque import Deque
    dq = Deque()
    assert type(dq) == Deque
