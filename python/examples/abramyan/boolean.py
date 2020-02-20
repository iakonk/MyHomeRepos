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


def bool_15(a, b, c):
    positive_cnt = 0
    positive_cnt = positive_cnt + 1 if a > 0 else positive_cnt
    positive_cnt = positive_cnt + 1 if b > 0 else positive_cnt
    positive_cnt = positive_cnt + 1 if c > 0 else positive_cnt
    return positive_cnt == 2


def bool_16(a):
    return a % 2 == 0 and 1 <= a // 10 <= 9


assert bool_16(99) == False
assert bool_16(100) == False
assert bool_16(10)


def bool_17(a):
    return a % 2 != 0 and 10 <= a // 10 <= 99


assert bool_17(999)
assert bool_17(1000) == False


def bool_18(a, b, c):
    return a == b or b == c


assert bool_18(3, 4, 4)


def bool_19(a, b, c):
    return a + b == 0 or b + c == 0


assert bool_19(2, -2, 1)


def bool_20(a, b, c):
    return a != b != c


assert bool_20(1, 2, 3)


def bool_21(num):
    """ 100 <= num < 1000 """
    first_n, sec_p = num // 100, num % 100
    sec_n, th_n = sec_p // 10, sec_p % 10
    return first_n < sec_n < th_n


assert bool_21(123)


def bool_22(num):
    first_n, sec_p = num // 100, num % 100
    sec_n, th_n = sec_p // 10, sec_p % 10
    # 123 or 321
    return first_n < sec_n < th_n or first_n > sec_n > th_n


assert bool_22(321)


def bool_23(num):
    """ 1000 <= num < 10000 """
    f_n = num // 1000
    s_n = num % 1000 // 100
    tr_n = num % 1000 % 100 // 10
    fs_n = num % 1000 % 100 % 10
    return f_n == fs_n and s_n == tr_n


assert bool_23(3223)