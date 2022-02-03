### Python LSD radix sort
def radixSort(a,n,maxLen):
    for x in range(maxLen):
        bins = [[] for i in range(n)]
        for y in a:
            bins[(y/n**x)%n].append(y)
        a=[]
        for section in bins:
            a.extend(section)
    return a

if __name__ == "__main__":
    import random
    import timeit
    a = [random.randint(0,10000) for i in xrange(1000000)]
    t = timeit.Timer('radixSort(a, 10, 5)', 'from __main__ import radixSort, a')
    print t.timeit(number=1)

### Compact version
def flatten(l):
    return [y for x in l for y in x]


def radix(l, p=None, s=None):
    if s == None:
        s = len(str(max(l)))
    if p == None:
        p = s

    i = s - p

    if i >= s:
        return l

    bins = [[] for _ in range(10)]

    for e in l:
        bins[int(str(e).zfill(s)[i])] += [e]

    return flatten([radix(b, p - 1, s) for b in bins]

### Comment version
def flatten(some_list):
    """
    Flatten a list of lists.
    Usage: flatten([[list a], [list b], ...])
    Output: [elements of list a, elements of list b]
    """
    new_list = []
    for sub_list in some_list:
        new_list += sub_list
    return new_list


def radix(some_list, idex=None, size=None):
    """
    Recursive radix sort
    Usage: radix([unsorted list])
    Output: [sorted list]
    """
    # Initialize variables not set in the initial call
    if size == None:
        largest_num = max(some_list)
        largest_num_str = str(largest_num)
        largest_num_len = len(largest_num_str)
        size = largest_num_len

    if idex == None:
        idex = size

    # Translate the index we're looking at into an array index.
    # e.g., looking at the 10's place for 100:
    # size: 3
    # idex: 2
    #    i: (3-2) == 1
    # str(123)[i] -> 2
    i = size - idex

    # The recursive base case.
    # Hint: out of range indexing errors
    if i >= size:
        return some_list

    # Initialize the bins we will place numbers into
    bins = [[] for _ in range(10)]

    # Iterate over the list of numbers we are given
    for e in some_list:
        # The destination bin; e.g.,:
        #   size: 5
        #      e: 29
        #  num_s: '00029'
        #      i: 3
        # dest_c: '2'
        # dest_i: 2
        num_s = str(e).zfill(size)
        dest_c = num_s[i]
        dest_i = int(dest_c)
        bins[dest_i] += [e]

    result = []
    for b in bins:
        # If the bin is empty it skips the recursive call
        if b == []:
            continue
        # Make the recursive call
        # Sort each of the sub-lists in our bins
        result.append(radix(b, idex - 1, size))

    # Flatten our list
    # This is also called in our recursive call,
    # so we don't need flatten to be recursive.
    flattened_result = flatten(result)

    return flattened_result