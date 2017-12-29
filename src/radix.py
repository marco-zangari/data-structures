"""Implement radix sort function."""


def radix_sort(unsorted, base=10):
    """Sort unsorted numbers in list working right- to left-most digit."""
    holder_list = []
    nth_place = len(str(max(unsorted)))
    if nth_place < 10:
        str_nth = '0' + str(nth_place)
    else:
        str_nth = str(nth_place)
    for num in unsorted:
        reformatted_num = format((num), str_nth)
        holder_list.append(reformatted_num)  #  all numbers same length, stringified with zeros in front

    new_nth_place = int(nth_place)
    while int(new_nth_place) > 0:

        buckets = [[] for _ in range(base)]
        temporary = buckets
        iteration = base ** int(new_nth_place - 1)
        for num in holder_list:
            nearly_sort = int(num) // iteration
            placement = str(nearly_sort)[-1]
            temporary[int(placement)].append(num)

        for sub_list in temporary:
            import pdb; pdb.set_trace()
            temp_list = []
            for item in range(sub_list):
                if sub_list is not None:
                    returned_item = sub_list.pop()
                    temp_list.append(returned_item)
        holder_list = temp_list
    new_nth_place -= 1

# unsorted = [170, 45, 75, 90, 2, 802, 2, 66]
