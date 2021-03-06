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


def test_hash_table_bucket_number():
    """Test number of buckets in hashTable."""
    from hash_table import HashTable
    h = HashTable(11, 1)
    assert h.buckets == [[], [], [], [], [], [], [], [], [], [], []]


def test_set_appends_key_value():
    """Test set method sets key and value."""
    from hash_table import HashTable
    h = HashTable(11)
    h.set('jackie', 'robinson')
    assert h.buckets == [[], [], [], [], [], [], [], [], [], [], [('jackie', 'robinson')]]


def test_set_appends_overrides_initial_value():
    """Test set method overrides another value."""
    from hash_table import HashTable
    h = HashTable(11)
    h.set('jackie', 'robinson')
    h.set('jackie', 'murray')
    assert h.buckets == [[], [], [], [], [], [], [], [], [], [], [('jackie', 'murray')]]


def test_set_returns_key():
    """Test get returns the key."""
    from hash_table import HashTable
    h = HashTable(11)
    h.set('jackie', 'robinson')
    h.set('jackie', 'murray')
    assert h.get('jackie') == 'murray'


def test_get_returns_val():
    """Test get returns the None if no value present."""
    from hash_table import HashTable
    h = HashTable(11)
    h.set('jackie', 'murray')
    assert h.get('jackie') == 'murray'


def test_djb_hash_loads_to_hashtable():
    """Test the djb hash function."""
    from hash_table import HashTable, djb_hash
    h = HashTable(11, djb_hash)
    h.set('jackie', 'robinson')
    assert h.get('jackie') == 'robinson'
