"""Test hash table."""

import pytest


def test_hash_table():
    """Test HashTable an instance."""
    from hash_table import HashTable
    h = HashTable(11, 1)
    assert isinstance(h, HashTable)


def test_hash_table_size():
    """Test HashTable has size 1."""
    from hash_table import HashTable
    h = HashTable(11, 1)
    assert h.size == 11
