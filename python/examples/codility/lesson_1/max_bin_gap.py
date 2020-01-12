"""
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded
by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2.
The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3.
The number 20 has binary representation 10100 and contains one binary gap of length 1.
The number 15 has binary representation 1111 and has no binary gaps.
The number 32 has binary representation 100000 and has no binary gaps.

Write a function:

    class Solution { public int solution(int N); }

that, given a positive integer N, returns the length of its longest binary gap.
The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and
so its longest binary gap is of length 5. Given N = 32 the function should return 0,
because N has binary representation '100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:
    N is an integer within the range [1..2,147,483,647].
"""


def is_last_bit_non_zero(positive_number):
    """
      11101010
      &
      00000001
      --------
    = 00000000
                OR
      11101011
      &
      00000001
      --------
    = 00000001
    """
    return positive_number & 1


def do_right_shift(positive_number):
    return positive_number >> 1


def find_max_bin_gap(positive_number):
    prev_non_zero_ind = None
    current_ind = 0
    max_gap = 0

    while positive_number > 0:

        if is_last_bit_non_zero(positive_number):
            if prev_non_zero_ind is not None:
                max_gap = max(max_gap, current_ind - prev_non_zero_ind - 1)
            prev_non_zero_ind = current_ind

        current_ind += 1
        positive_number = do_right_shift(positive_number)

    return max_gap


assert find_max_bin_gap(9) == 2, find_max_bin_gap(9)  # 1001
assert find_max_bin_gap(529) == 4, find_max_bin_gap(529)  # 1000010001
assert find_max_bin_gap(20) == 1, find_max_bin_gap(20)  # 10100
assert find_max_bin_gap(15) == 0, find_max_bin_gap(15)  # 1111
assert find_max_bin_gap(32) == 0, find_max_bin_gap(32)  # 100000
assert find_max_bin_gap(1041) == 5, find_max_bin_gap(1041)  # 10000010001
