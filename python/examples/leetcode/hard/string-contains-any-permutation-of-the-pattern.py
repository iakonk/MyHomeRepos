# Given a string and a pattern, find out if the string contains any permutation of the pattern.
# Permutation is defined as the re-arranging of the characters of the string. For example, “abc”
# has the following six permutations:
# abc
# acb
# bac
# bca
# cab
# cba

# Input: String="oidbcaf", Pattern="abc"
# Output: true
# Explanation: The string contains "bca" which is a permutation of the given pattern.

import collections


def find_permutation(str, pattern):
    aggr_p = collections.Counter(pattern)
    tail = match = 0

    for head, char in enumerate(str):
        if char in aggr_p:
            aggr_p[char] -= 1
            match += aggr_p[char] == 0
        if match == len(aggr_p):
            return True
        while match > 0 and (char not in aggr_p or aggr_p[char] < 0):
            if str[tail] in aggr_p:
                if aggr_p[str[tail]] == 0:
                    match -= 1
                aggr_p[str[tail]] += 1
            tail += 1
    return False


ans = find_permutation("bcdxabcdy", "bcdyabcdx")
assert ans

ans = find_permutation("oidbcaf", "abc")
assert ans

ans = find_permutation("odicf", "dc")
assert not ans