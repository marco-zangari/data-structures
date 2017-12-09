"""Implementation for a merge sort, hat tip John von Neumann, cs legend."""


def merge_sort(seq):
    """Merge and sort algorithm."""
    mid = len(seq) // 2
    lft, rgt = seq[:mid], seq[mid:]
    if len(lft) > 1:
        lft.merge_sort(lft)
    if len(rgt) > 1:
        rgt.merge_sort(rgt)
    res = []
    while lft and rgt:
        if lft[-1] >= rgt[-1]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())
    res.reverse()
    return (lft or rgt) + res

