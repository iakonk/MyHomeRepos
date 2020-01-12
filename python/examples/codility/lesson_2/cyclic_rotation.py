"""
An array A consisting of N integers is given. Rotation of the array means that each element is shifted right
by one index, and the last element of the array is moved to the first place. For example,
the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index
and 6 is moved to the first place).

The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.

Write a function:

    def solution(A, K)

that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.

For example, given
    A = [3, 8, 9, 7, 6]
    K = 3
the function should return [9, 7, 6, 3, 8]. Three rotations were made:
    [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
    [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
    [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
"""


def reverse_the_array(array):
    for i in range(0, len(array) // 2):
        k = len(array) - i - 1
        array[i], array[k] = array[k], array[i]
    return array


assert reverse_the_array([1, 2, 3, 4]) == [4, 3, 2, 1]
assert reverse_the_array([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]


def rotate_the_array(array, rotations_num):
    for i in range(0, rotations_num):
        last_elem = array.pop()
        array.insert(0, last_elem)
    return array


assert rotate_the_array([3, 8, 9, 7, 6], 3) == [9, 7, 6, 3, 8], rotate_the_array([3, 8, 9, 7, 6], 3)
assert rotate_the_array([0, 0, 0], 1) == [0, 0, 0], rotate_the_array([0, 0, 0], 1)
assert rotate_the_array([1, 2, 3, 4], 4) == [1, 2, 3, 4], rotate_the_array([1, 2, 3, 4], 4)
