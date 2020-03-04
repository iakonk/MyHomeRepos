def find_average(k, array):
    result = []
    start, window_sum = 0, 0

    for ind in range(0, len(array)):
        window_sum += array[ind]

        if ind >= k - 1:
            result.append(window_sum / k)
            window_sum -= array[start]
            start += 1
    return result


assert find_average(5, [1, 3, 2, 6, -1, 4, 1, 8, 2]) == [2.2, 2.8, 2.4, 3.6, 2.8]


def max_sub_array_of_size_k(k, arr):
    max_sum, start = 0, 0

    window_sum = 0
    for ind in range(0, len(arr)):
        window_sum += arr[ind]

        if ind >= k - 1:
            if window_sum > max_sum:
                max_sum = window_sum
            window_sum -= arr[start]
            start += 1
    return max_sum


assert max_sub_array_of_size_k(2, [2, 3, 4, 1, 5]) == 7


def smallest_subarr_with_given_sum(sum_, array):
    window_sum = 0
    window_min_len = array[0]
    window_start = 0

    for ind in range(0, len(array)):
        window_sum += array[ind]

        while window_sum >= sum_:
            window_min_len = min(window_min_len, ind - window_start + 1)
            window_sum -= array[window_start]
            window_start += 1
    return window_min_len


assert smallest_subarr_with_given_sum(7, [2, 1, 5, 2, 3, 2]) == 2
assert smallest_subarr_with_given_sum(7, [2, 1, 5, 2, 8]) == 1
assert smallest_subarr_with_given_sum(8, [3, 4, 1, 1, 6]) == 3