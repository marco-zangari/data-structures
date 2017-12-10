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

    a_list = [4, 3, 7, 6]
    b_list = [72, 4, 10, 6, 20, 18, 91, 45, 3, 15]
    c_list = [list(range(100, 0, -1))]

    time_a = ti.timeit("insertion_sort(a_list)",
    setup = "from __main__ import a_list, insertion_sort")

    time_b = ti.timeit("insertion_sort(b_list)",
    setup = "from __main__ import b_list, insertion_sort")

    time_c = ti.timeit("insertion_sort(c_list)",
    setup = "from __main__ import c_list, insertion_sort")

    print(f"""
These are insertion sort times for different kinds of lists:\
one short, one longer, and one longer still.

Input: [4, 3, 7, 6]
Output: { time_a }

Input: [72, 4, 10, 6, 20, 18, 91, 45, 3, 15]
Output: { time_b }

Input (list(range(100, 0, -1)))
Output: { time_c }.""")
