"""Implement radix sort function."""


def radix_sort(unsorted, base=10):
    """Sorts unsorted numbers in list working right- to left-most digit."""
    holder_list = []
    temp_list = []
    buckets = [[] for _ in range(base)]
    nth_place = len(str(max(unsorted)))
    iteration = base ** (nth_place - 1)
    if nth_place < 10:
        str_nth = '0' + str(nth_place)
    else:
        str_nth = str(nth_place)
    for num in unsorted:
        reformatted_num = format((num), str_nth)
        holder_list.append(reformatted_num) #  all numbers same length, stringified with zeros in front

    nth_place = int(nth_place)
    while int(nth_place) > 0:

        for num in holder_list:
            nearly_sort = num // (base ** (int(nth_place) - 1)
            placement = str(nearly_sort)[-1]
            buckets[int(placement) - 1].append(num)

            for bucket in buckets:

            holder_list = []

        int(nth_place) -= 1


unsorted = [170, 45, 75, 90, 2, 802, 2, 66]
