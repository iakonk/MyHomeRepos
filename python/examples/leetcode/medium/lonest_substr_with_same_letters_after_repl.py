def longest_substr(string, k):
    left = max_unique = max_repeat_letter_count = 0
    aggr_chars = {}

    for right, char in enumerate(string):
        aggr_chars.setdefault(char, 0)
        aggr_chars[char] += 1
        max_freq = max(max_unique, aggr_chars[char])

        all_chars_before = right - left + 1
        to_replace = all_chars_before - max_freq
        if to_replace > k:
            left_char = string[left]
            aggr_chars[left_char] -= 1
            left += 1
        max_repeat_letter_count = max(max_repeat_letter_count, right - left + 1)
    return max_repeat_letter_count


ans = longest_substr("aabccbb", 2)
print(ans)
