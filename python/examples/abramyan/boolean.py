def bool_1(number):
    return number > 0


def bool_2(num):
    return num % 2 > 0


def bool_3(num):
    return num % 2 == 0


def bool_4(a, b):
    return a > 2 and b <= 3


def bool_5(a, b):
    return a >= 0 and b < -2


def bool_6(a, b, c):
    return a < b < c


def bool_7(a, b, c):
    return a <= b <= c


def bool_8(a, b):
    return a % 2 > 0 and b % 2 > 0


def bool_9(a, b):
    return a % 2 > 0 or b % 2 > 0


def bool_10(a, b):
    odd_cnt = 0
    odd_cnt = odd_cnt + 1 if a % 2 > 0 else odd_cnt
    odd_cnt = odd_cnt + 1 if b % 2 > 0 else odd_cnt
    return odd_cnt == 1


assert bool_10(3, 7) == False
assert bool_10(3, 4) == True
assert bool_10(4, 3) == True
assert bool_10(4, 4) == False


def bool_11(a, b):
    is_a_odd = a % 2 > 0
    is_b_odd = b % 2 > 0

    odd_cnt = 0
    odd_cnt = odd_cnt + 1 if is_a_odd and is_b_odd else odd_cnt
    odd_cnt = odd_cnt + 1 if not is_a_odd and not is_b_odd else odd_cnt
    return odd_cnt == 1


assert bool_11(3, 3)
assert bool_11(4, 4)
assert bool_11(3, 4) == False
assert bool_11(4, 3) == False


def bool_12(a, b, c):
    return a > 0 and b > 0 and c > 0


def bool_13(a, b, c):
    return a > 0 or b > 0 or c > 0


def bool_14(a, b, c):
    pos_cnt = 0
    pos_cnt = pos_cnt + 1 if a >= 0 else pos_cnt
    pos_cnt = pos_cnt + 1 if b >= 0 else pos_cnt
    pos_cnt = pos_cnt + 1 if c >= 0 else pos_cnt
    return pos_cnt == 1


assert bool_14(0, -1, -1)
assert bool_14(0, 0, 0) == False