"""Quick sort implementation."""


def quick_sort(alist):
    """Implement a sorted in order by value list."""
    if len(alist) < 2:
        return alist
    if len(alist) == 2:
        if alist[0] > alist[1]:
            alist[0], alist[1] = alist[1], alist[0]
        return alist
    pivot = alist[0]
    less = []
    greater = []
    for num in alist:
        if num < pivot:
            less.append(num)
        if num > pivot:
            greater.append(num)
    return quick_sort(less) + [pivot] + quick_sort(greater)

if __name__ == '__main__':
    import timeit as ti

    a_list = [4, 3, 7, 6]
    b_list = [72, 4, 10, 6, 20, 18, 91, 45, 3, 15]
    c_list = [list(range(100, 0, -1))]

    time_a = ti.timeit("quick_sort(a_list)",
    setup = "from __main__ import a_list, quick_sort")

    time_b = ti.timeit("quick_sort(b_list)",
    setup = "from __main__ import b_list, quick_sort")

    time_c = ti.timeit("quick_sort(c_list)",
    setup = "from __main__ import c_list, quick_sort")

    print(f"""
These are quick sort times for different kinds of lists:\
one short, one longer, and one longer still.

Input: [4, 3, 7, 6]
Output: { time_a }

Input: [72, 4, 10, 6, 20, 18, 91, 45, 3, 15]
Output: { time_b }

Input (list(range(100, 0, -1)))
Output: { time_c }.""")
