def max_len_of_unique_substr(charactres):
    indexes_map = {}
    left, max_len = 0, 0

    for right, char in enumerate(charactres):
        if char in indexes_map:
            left = max(left, indexes_map[char] + 1)
        indexes_map[char] = right
        max_len = max(max_len, right - left + 1)
    return max_len


ans = max_len_of_unique_substr("aabccbb")
print(ans)
