"""Implement radix sort function, hattip geekviewpoint."""

from decimal import Decimal

def radix_sort(alist):
    """Sort a list of numbers in list."""
    radix = 10
    maxLength = False
    tmp, placement = -1, 1

    while not maxLength:
        maxLength = True
        buckets = [[] for _ in range(radix)]
        for i in alist:
            tmp = i / placement
            buckets[int(tmp) % radix].append(i)
            if maxLength and tmp > 0:
                maxLength = False
        a = 0
        for b in range(radix):
            buck = buckets[b]
            for i in buck:
                alist[a] = i
                a += 1
        placement *= radix
    return alist

if __name__ == '__main__':
    import timeit as ti

    a_list = [4, 3, 7, 6]
    b_list = [72, 4, 10, 6, 20, 18, 91, 45, 3, 15]
    c_list = [list(range(100, 0, -1))]

    time_a = ti.timeit("radix_sort(a_list)",
    setup = "from __main__ import a_list, radix_sort")

    time_b = ti.timeit("radix_sort(b_list)",
    setup = "from __main__ import b_list, radix_sort")

    time_c = ti.timeit("radix_sort(c_list)",
    setup = "from __main__ import c_list, radix_sort")

    print(f"""
These are radix sort times for different kinds of lists:\
one short, one longer, and one longer still.

Input: [4, 3, 7, 6]
Output: { time_a }

Input: [72, 4, 10, 6, 20, 18, 91, 45, 3, 15]
Output: { time_b }

Input (list(range(100, 0, -1)))
Output: { time_c }.""")
