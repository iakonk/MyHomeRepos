
def find_permutation(string, pattern):
    pattern_set = set(pattern)
    start_ind = matched_chars_c = 0
    pattern_len = len(pattern)

    for ind in range(len(string)):
        curr_char = string[ind]

        if curr_char in pattern_set:
            matched_chars_c += 1
        if matched_chars_c == pattern_len:
            return True

        if ind - start_ind + 1 >= pattern_len:
            matched_chars_c = 0
            start_ind = min(ind + 1, len(string))

    return matched_chars_c == pattern_len


assert find_permutation("oidbcaf", "abc")
assert find_permutation("bcdxabcdy", "bcdyabcdx")
assert find_permutation("aaacb", "abc")
assert find_permutation("odicf", "dc") == False
