"""
Given an array of strings, return the longest common prefix that is shared amongst all strings.
Note: you may assume all strings only contain lowercase alphabetical characters.

Ex: Given the following arrays...

["colorado", "color", "cold"], return "col"
["a", "b", "c"], return ""
["spot", "spotty", "spotted"], return "spot"
"""


class Solution(object):
    def longest_common_prefix(self, arr):
        def find_longest_pref(prev_w, curr_w):
            longest_pref = ""
            for l_c, r_c in zip(prev_w, curr_w):
                if l_c == r_c:
                    longest_pref += l_c
                else:
                    break
            return longest_pref

        if len(arr) == 1:
            return arr[0]
        elif not len(arr):
            return ""

        longest_pref = ""
        for i, word in enumerate(arr, 1):
            prev_w = arr[i-1]
            p = find_longest_pref(prev_w, word)
            if len(p) <= len(longest_pref):
                longest_pref = p
        return longest_pref


assert Solution().longest_common_prefix(["a", "b", "c"],) == ""
assert Solution().longest_common_prefix(["colorado", "color", "cold"]) == "col"
