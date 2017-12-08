"""Implement bubble sort."""


def bubble_sort(alist):
    """Implement a bubble sort."""
    potato = True
    while potato:
        potato = False
        for idx in range(len(alist) - 1):
            if alist[idx] > alist[idx + 1]:
                temp = alist[idx]
                alist[idx] = alist[idx + 1]
                alist[idx + 1] = temp
                potato = True
    return alist

if __name__ == '__main__':
    import timeit as ti

    a_list = [4, 3, 7, 6]
    b_list = [72, 4, 10, 6, 20, 18, 91, 45, 3, 15]
    c_list = [list(range(100, 0, -1))]

    time_a = ti.timeit("bubble_sort(a_list)"),
    setup = "from __main__ import a_list, bubble_sort"

    time_b = ti.timeit("bubble_sort(b_list"),
    setup = "from __main__ import b_list, bubble_sort"

    time_c = ti.timeit("bubble_sort(c_list"),
    setup = "from __main__ import c_list, bubble_sort"

    print(f"""
These are bubble sort times for different kinds of lists:\
one short, one longer, and one longer still.

Input: [4, 3, 7, 6]
Output: { time_a }

Input: [72, 4, 10, 6, 20, 18, 91, 45, 3, 15]
Output: { time_b }

Input (list(range(100, 0, -1)))
Output: { time_c }
        .""")
