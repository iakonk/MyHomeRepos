"""
Given an array nums of integers, return how many of them contain an even number of digits.
Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation:
12 contains 2 digits (even number of digits).
345 contains 3 digits (odd number of digits).
2 contains 1 digit (odd number of digits).
6 contains 1 digit (odd number of digits).
7896 contains 4 digits (even number of digits).
Therefore only 12 and 7896 contain an even number of digits.

https://ru.wikipedia.org/wiki/%D0%94%D0%B5%D1%81%D1%8F%D1%82%D0%B8%D1%87%D0%BD%D1%8B%D0%B9_%D0%BB%D0%BE%D0%B3%D0%B0%D1%80%D0%B8%D1%84%D0%BC
log10(10) = 1  # The result is 1 since 10^1=10.
log10(100) = 2 # The result is 2 since 10^2=100.
"""
import math


def nums_with_even_num_of_digits_v1(nums_array):
    count = 0
    for num in nums_array:
        is_even = (math.floor(math.log(num, 10)) + 1) % 2 == 0
        if is_even:
            count += 1
    return count


assert nums_with_even_num_of_digits_v1([1, 2, 3, 4, 5, 10, 11]) == 2


def nums_with_even_num_of_digits_v2(nums_array):
    return sum([(math.floor(math.log(num, 10)) + 1) % 2 == 0 for num in nums_array])


assert nums_with_even_num_of_digits_v2([1, 2, 3, 4, 5, 10, 11]) == 2
