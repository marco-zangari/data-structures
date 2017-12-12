"""Quick sort implementation."""


def quick_sort(alist):
    """Implement a sorted in order by value list."""
    if len(alist) < 2:
        return alist
    if len(alist) == 2:
        if alist[0] > alist[1]:
            alist[0], alist[1] = alist[1], alist[0]
        return alist
    if len(alist) > 2:
