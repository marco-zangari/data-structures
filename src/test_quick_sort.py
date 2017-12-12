"""Test quick sort implementation."""

import pytest

from quick_sort import quick_sort


def test_quick_sort_short_list():
    """Test quick with small list."""
    short_list = [4, 3, 7, 6]
    assert quick_sort(short_list) == [3, 4, 6, 7]


def test_quick_sort_long_list():
    """Test quick with long list."""
    long_list = [72, 4, 10, 6, 20, 18, 91, 45, 3, 15]
    assert quick_sort(long_list) == [3, 4, 6, 10, 15, 18, 20, 45, 72, 91]


def test_quick_sort_negative_num():
    """Test quick sort works with negative numbers."""
    list_negative_num = [72, 4, -6]
    assert quick_sort(list_negative_num) == [-6, 4, 72]


def test_quick_sort_decimals():
    """Test quick sort takes a decimal float."""
    list_decimals = [5.5, 5.3, 5.2, 4]
    assert quick_sort(list_decimals) == [4, 5.2, 5.3, 5.5]
