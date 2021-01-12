def shortest_window_sort(arr):
    lo, hi = 0, len(arr) - 1

    # find the first elem out of order
    while lo < hi and arr[lo] <= arr[lo + 1]:
        lo += 1

    if lo == len(arr) - 1:
        return 0

    while hi > 0 and arr[hi] >= arr[hi - 1]:
        hi -= 1

    max_elem = -float('inf')
    min_elem = float('inf')

    for i in range(lo, hi + 1):
        max_elem = max(max_elem, arr[i])
        min_elem = min(min_elem, arr[i])

    while lo > 0 and arr[lo - 1] > min_elem:
        lo -= 1

    while hi < len(arr) - 1 and arr[hi + 1] < max_elem:
        hi += 1

    return hi - lo + 1
