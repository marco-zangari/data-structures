"""Implement radix sort function."""


def radix_sort(unsorted, base=10):
    """Sorts unsorted numbers in list working right- to left-most digit."""
    holder_list = []
    temp_list = []
    buckets = [[] for _ in range(base)]
    nth_place = len(str(max(unsorted)))
    if nth_place < 10:
        str_nth = '0' + str(nth_place)
    for num in unsorted:
        reformatted_num = format((num), str_nth)
        holder_list.append(reformatted_num)



unsorted = [170, 45, 75, 90, 2, 802, 2, 66]
