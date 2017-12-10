"""Insertion sort implementation.

Inspiration from: http://www.geekviewpoint.com/python/sorting/insertionsort."""


def insertion_sort(list_obj):
    """Insert a list to be ordered."""
    for i in range(1, len(list_obj)):
        current = list_obj[i]
        while i > 0 and list_obj[i - 1] > current:
            list_obj[i] = list_obj[i - 1]
            i = i - 1
            list_obj[i] = current
    return list_obj
