"""
Partition of a set into K subsets with equal sum
Given an integer array of N elements, the task is to divide this array into K non-empty subsets such that the
sum of elements in every subset is same. All elements of this array should be part of exactly one partition.
Examples:

Input : arr = [2, 1, 4, 5, 6], K = 3
Output : Yes
we can divide above array into 3 parts with equal
sum as [[2, 4], [1, 5], [6]]

Input  : arr = [2, 1, 5, 5, 6], K = 3
Output : No
It is not possible to divide above array into 3
parts with equal sum
"""


def is_equal_sum_possible(array):
    if not array or len(array) == 1:
        return False

    left_sum = array[0]
    right_sum = sum(array[1:])
    if left_sum == right_sum:
        return array[0], array[1:]

    curr_index = 0
    for elem in array[1:]:
        curr_index += 1
        left_sum += elem
        right_sum -= elem

        if left_sum == right_sum:
            return array[:curr_index + 1], array[curr_index + 1:]

    return False


assert is_equal_sum_possible([2, 1, 4, 5, 6]) == False
assert is_equal_sum_possible([1, 1, 1, 3]) == ([1, 1, 1], [3])
