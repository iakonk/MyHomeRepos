def max_len_of_unique_substr(charactres):
    indexes_map = {}
    window_start, max_len = 0, 0

    for window_end in range(len(charactres)):
        right_char = charactres[window_end]

        if right_char in indexes_map:
            window_start = max(window_start, indexes_map[right_char] + 1)
        indexes_map[right_char] = window_end
        max_len = max(max_len, window_end - window_start + 1)
    return max_len

ans = max_len_of_unique_substr("aabccbb")
print(ans)
