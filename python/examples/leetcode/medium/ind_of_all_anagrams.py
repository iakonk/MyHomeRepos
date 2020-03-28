import collections


def find_string_anagrams(str, pattern):
    window_start, matched = 0, 0
    char_frequency = collections.Counter(pattern)

    result_indices = []
    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1

        if matched == len(char_frequency):  # Have we found an anagram?
            result_indices.append(window_start)

        # Shrink the sliding window
        if window_end >= len(pattern) - 1:
            left_char = str[window_start]
            window_start += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1  # Before putting the character back, decrement the matched count
                char_frequency[left_char] += 1  # Put the character back

    return result_indices


ans = find_string_anagrams("ppqp", "pq")
print(ans)
