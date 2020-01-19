def quicksort(lst):
    """
    Sorts an array in the ascending order in O(n log n) time
    :param nums: a list of numbers
    :return: the sorted list
    """
    if not lst:
        return None

    n = len(lst)
    qsort(lst, 0, n - 1)


def qsort(self, lst, lo, hi):

    if lo < hi:
        p = partition(lst, lo, hi)
        qsort(lst, lo, p - 1)
        qsort(lst, p + 1, hi)


def partition(lst, lo, hi):
    pivot = lst[hi]
    i = lo

    for j in range(lo, hi):
        if lst[j] < pivot:
            lst[i], lst[j] = lst[j], lst[1]
            i += 1

    lst[i], lst[hi] = lst[hi], lst[i]
    return i
