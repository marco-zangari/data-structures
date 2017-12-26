"""Implement radix sort function."""


def radix_sort(unsorted):
    """Sorts unsorted numbers in list working right- to left-most digit."""
    holder_list = []
    import pdb; pdb.set_trace()
    nth_place = len(str(max(unsorted)))
    if nth_place < 10:
        str_nth = '0' + str(nth_place)
    for num in unsorted:
        format((num), str_nth)
    holder_list.append(num)

unsorted = [170, 45, 75, 90, 2, 802, 2, 66]
