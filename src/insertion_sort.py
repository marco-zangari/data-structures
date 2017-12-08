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


if __name__ == '__main__':
    import timeit as ti
    list1 = [4, 3, 7, 6]
    list2 = [72, 4, 10, 6, 20, 18, 91, 45, 3, 15]
    list3 = list(range(100)) for

