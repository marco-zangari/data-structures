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
        pivot = alist[0]
        less = []
        greater = []
        for num in range(len(alist) - 1):
            if num > pivot:
                less.append(num)
            if num < pivot:
                greater.append(num)
