"""Implement radix sort function."""


def radix_sort(unsorted):
    """Sorts unsorted numbers in list working right- to left-most digit."""
    holder_list = []
    nth_place = len(str(max(unsorted)))
    for num in unsorted:
        format((num), nth_place)
    holder_list.append
