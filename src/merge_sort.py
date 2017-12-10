"""Implementation for a merge sort, hat tip John von Neumann, cs legend."""


def merge_sort(seq):
    """Merge and sort algorithm."""
    mid = len(seq) // 2
    lft, rgt = seq[:mid], seq[mid:]
    if len(lft) > 1:
        lft = merge_sort(lft)
    if len(rgt) > 1:
        rgt = merge_sort(rgt)
    res = []
    while lft and rgt:
        if lft[-1] >= rgt[-1]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())
    res.reverse()
    return (lft or rgt) + res

if __name__ == '__main__':
    import timeit as ti

    a_list = [4, 3, 7, 6]
    b_list = [72, 4, 10, 6, 20, 18, 91, 45, 3, 15]
    c_list = [list(range(100, 0, -1))]

    time_a = ti.timeit("merge_sort(a_list)",
    setup = "from __main__ import a_list, merge_sort")

    time_b = ti.timeit("merge_sort(b_list)",
    setup = "from __main__ import b_list, merge_sort")

    time_c = ti.timeit("merge_sort(c_list)",
    setup = "from __main__ import c_list, merge_sort")

    print(f"""
These are merge sort times for different kinds of lists:\
one short, one longer, and one longer still.

Input: [4, 3, 7, 6]
Output: { time_a }

Input: [72, 4, 10, 6, 20, 18, 91, 45, 3, 15]
Output: { time_b }

Input (list(range(100, 0, -1)))
Output: { time_c }
        .""")
