"""
Given an array of lowercase letters sorted in ascending order,
find the smallest letter in the given array greater than a given ‘key’.

Assume the given array is a circular list, which means that the last letter is assumed to be
connected with the first letter. This also means that the smallest letter in the given array is greater than the
last letter of the array and is also the first letter of the array.

Write a function to return the next letter of the given ‘key’.

Example 1:

Input: ['a', 'c', 'f', 'h'], key = 'f'
Output: 'h'
Explanation: The smallest letter greater than 'f' is 'h' in the given array.
"""


class Solution(object):
    def findNextLetter(self, arr, key):
        first, last = arr[0], arr[-1]
        if key > last or key < first:
            return first

        start, end = 0, len(arr) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if key < arr[mid]:
                end = mid - 1
            else:
                # key  >= mid
                start = mid + 1

        return arr[start % len(arr)]


assert Solution().findNextLetter(['a', 'c', 'f', 'h'], 'f') == 'h'
assert Solution().findNextLetter(['a', 'c', 'f', 'h'], 'h') == 'a'
assert Solution().findNextLetter(['a', 'c', 'f', 'h'], 'b') == 'c'