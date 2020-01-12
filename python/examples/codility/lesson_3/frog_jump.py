"""
A small frog wants to get to the other side of the road. The frog is currently located at position X and wants to get
to a position greater than or equal to Y. The small frog always jumps a fixed distance, D.

Count the minimal number of jumps that the small frog must perform to reach its target.

Write a function:

    def solution(X, Y, D)

that, given three integers X, Y and D, returns the minimal number of jumps from position X to a position equal to or greater than Y.

For example, given:
  X = 10
  Y = 85
  D = 30
the function should return 3, because the frog will be positioned as follows:

after the first jump, at position 10 + 30 = 40
after the second jump, at position 10 + 30 + 30 = 70
after the third jump, at position 10 + 30 + 30 + 30 = 100
Write an efficient algorithm for the following assumptions:

X, Y and D are integers within the range [1..1,000,000,000];
X ≤ Y.
"""


def count_min_jumps_number_v1(curr_pos, target_pos, fixed_distance):
    jumps_count = 0

    while curr_pos < target_pos:
        curr_pos += fixed_distance
        jumps_count += 1
    return jumps_count


assert count_min_jumps_number_v1(10, 85, 30) == 3,  count_min_jumps_number_v1(10, 85, 30)


def count_min_jumps_number_v2(curr_pos, target_pos, fixed_distance):
    distance_left = target_pos - curr_pos
    jumps_left = distance_left // fixed_distance
    return jumps_left + 1 if distance_left % fixed_distance > 0 else jumps_left


assert count_min_jumps_number_v2(10, 85, 30) == 3,  count_min_jumps_number_v1(10, 85, 30)
