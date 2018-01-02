"""Test radix sort algorithm."""

from random import randint
import pytest

from radix import radix_sort


def test_radix_sort_no_objs():
    """Test radix works with an empty list."""
    no_list = []
    assert radix_sort(no_list) == []


def test_radix_sort_short_list():
    """Test radix with small list."""
    short_list = [4, 3, 7, 6]
    assert radix_sort(short_list) == [3, 4, 6, 7]


def test_radix_sort_long_list():
    """Test radix with long list."""
    long_list = [72, 4, 10, 6, 20, 18, 91, 45, 3, 15]
    assert radix_sort(long_list) == [3, 4, 6, 10, 15, 18, 20, 45, 72, 91]


def test_radix_sort_sorted_list():
    """Test radix with an already sorted list."""
    sorted_list = [1, 2, 3, 4, 5, 6, 7, 88, 104, 224]
    assert radix_sort(sorted_list) == [1, 2, 3, 4, 5, 6, 7, 88, 104, 224]


def test_radix_sort_with_random_generate_list():
    """Test random generated list of hundred returns sorted."""
    rando_list = [randint(1, 100000) for x in range(100)]
    assert radix_sort(rando_list) == sorted(rando_list)
