"""Test the insertion sort."""

import pytest

from insertion_sort import insertion_sort


def test_insertion_sort_short_list():
    """Test insertion with small list."""
    short_list = [4, 3, 7, 6]
    assert insertion_sort(short_list) == [3, 4, 6, 7]


def test_insertion_sort_long_list():
    """Test insertion with long list."""
    long_list = [72, 4, 10, 6, 20, 18, 91, 45, 3, 15]
    assert insertion_sort(long_list) == [3, 4, 6, 10, 15, 18, 20, 45, 72, 91]


def test_insertion_sort_negative_num():
    """Test insertion sort works with negative numbers."""
    list_negative_num = [72, 4, -6]
    assert insertion_sort(list_negative_num) == [-6, 4, 72]


def test_insertion_sort_decimals():
    """Test insertion sort takes a decimal float."""
    list_decimals = [5.5, 5.3, 5.2, 4]
    assert insertion_sort(list_decimals) == [4, 5.2, 5.3, 5.5]
