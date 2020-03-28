def longest_substr(string, k):
    window_start = max_unique = max_repeat_letter_count = 0
    aggr_chars = {}

    for window_end in range(len(string)):
        curr_char = string[window_end]
        aggr_chars.setdefault(curr_char, 0)
        aggr_chars[curr_char] += 1
        max_freq = max(max_unique, aggr_chars[curr_char])

        all_chars_before = window_end - window_start + 1
        to_replace = all_chars_before - max_freq
        if to_replace > k:
            left_char = string[window_start]
            aggr_chars[left_char] -= 1
            window_start += 1
        max_repeat_letter_count = max(max_repeat_letter_count, window_end - window_start + 1)
    return max_repeat_letter_count


ans = longest_substr("aabccbb", 2)
print(ans)
