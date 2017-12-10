"""Test the merge sort."""

import pytest

from merge_sort import merge_sort


def test_merge_sort_short_list():
    """Test merge with small list."""
    short_list = [4, 3, 7, 6]
    assert merge_sort(short_list) == [3, 4, 6, 7]


def test_merge_sort_long_list():
    """Test merge with long list."""
    long_list = [72, 4, 10, 6, 20, 18, 91, 45, 3, 15]
    assert merge_sort(long_list) == [3, 4, 6, 10, 15, 18, 20, 45, 72, 91]


def test_merge_sort_negative_num():
    """Test merge sort works with negative numbers."""
    list_negative_num = [72, 4, -6]
    assert merge_sort(list_negative_num) == [-6, 4, 72]


def test_merge_sort_decimals():
    """Test merge sort takes a decimal float."""
    list_decimals = [5.5, 5.3, 5.2, 4]
    assert merge_sort(list_decimals) == [4, 5.2, 5.3, 5.5]
