"""Implement radix sort function, hattip geekviewpoint."""


def radix_sort(unsorted):
    """Sort unsorted numbers in list working right- to left-most digit."""
    radix = 10
    maxLength = False
    tmp, placement = -1, 1

    while not MaxLength:
        maxLength = True
        buckets = [[] for _ in range(radix)]
        for i in unsorted:
            tmp = i / placement
            buckets[int(tmp) % radix].append(i)
            if maxLength and tmp > 0:
                maxLength = False
        a = 0
        for b in range(radix):
            buck = buckets[b]
            for i in buck:
                unsorted[a] = i
                a += 1
        placement *= radix


# unsorted = [170, 45, 75, 90, 2, 802, 2, 66]
