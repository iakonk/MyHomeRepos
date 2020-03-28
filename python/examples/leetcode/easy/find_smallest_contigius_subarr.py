def find_max_freq(arr):
    window_start, max_freq = 0, 0
    numbers_freq = {}

    for window_end in range(len(arr)):
        right_num = arr[window_end]
        numbers_freq.setdefault(right_num, 0)
        numbers_freq[right_num] += 1

        while len(numbers_freq) > 1:
            left_num = arr[window_start]
            numbers_freq[left_num] -= 1
            if numbers_freq[left_num] == 0:
                del numbers_freq[left_num]
            window_start += 1
        max_freq = max(max_freq, window_end - window_start + 1)
    return max_freq


ans = find_max_freq([1, 2, 2, 3, 1])
print(ans)
