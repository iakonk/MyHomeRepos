def find_full_units(init_num, unit):
    return init_num // unit


def find_reminder(init_num, unit):
    return init_num % unit


def find_quotient_and_reminder(init_num, unit):
    """ 10 <= init_num < 100"""
    return init_num // unit, init_num % unit


# Integer1. how many full meteres in L santimeters
ONE_METER = 100
assert find_full_units(200, ONE_METER) == 2
assert find_full_units(150, ONE_METER) == 1
assert find_full_units(90, ONE_METER) == 0

# Integer2. how many ton in M kg
ONE_TON = 1000
assert find_full_units(1050, ONE_TON) == 1

# Integer3. file size in bytes
ONE_KB = 1024
assert find_full_units(2048, ONE_KB) == 2
assert find_full_units(2047, ONE_KB) == 1

# Integer4. how many slices B in A.
assert find_full_units(10, 3) == 3

# Integer5. how much space is left
assert find_reminder(5, 4) == 1
assert find_reminder(3, 2) == 1

# Integer 6.
assert find_quotient_and_reminder(23, 10) == (2, 3)


# Integer 7.
def find_sum_and_mulp(init_num):
    """ 10 <= init_num < 100"""
    quotient, reminder = init_num // 10, init_num % 10
    return quotient + reminder, quotient * reminder


assert find_sum_and_mulp(23) == (5, 6)


# Integer 8.
def shuffle_int(num):
    """ 10 <= num < 100 """
    quotient, reminder = num // 10, num % 10
    return int('%s%s' % (reminder, quotient))


assert shuffle_int(54) == 45

# Integer 9. 100 <= num < 1000
find_hundreds = lambda x: x // 100
assert find_hundreds(300) == 3


# Integer 10. find units, dozens for 100 <= num < 1000
def find_units_and_dozens(num):
    dozens = num % 100
    units, dozens = dozens % 10, dozens // 10
    return units, dozens


assert find_units_and_dozens(123) == (3, 2)


def integer_11(num):
    """ 100 <= num < 1000 """
    hundreds = num // 100
    dozens = (num % 100) // 10
    units = (num % 100) % 10
    return hundreds + dozens + units, hundreds * dozens * units


assert integer_11(100) == (1, 0)
assert integer_11(350) == (8, 0)


def integer_12(num):
    """ 100 <= num < 1000 """
    hundreds = num // 100
    dozens = (num % 100) // 10
    units = (num % 100) % 10
    return int('%s%s%s' % (units, dozens, hundreds))


assert integer_12(300) == 3
assert integer_12(524) == 425


def integer_13(num):
    """ 100 <= num < 1000 """
    hundreds, dozens = num // 100, num % 100
    return int('%s%s' % (dozens, hundreds))


assert integer_13(534) == 345


def integer_14(num):
    """ 100 <= num < 1000 """
    hundreds, dozens, units = num // 100, num % 100, num % 100 % 10
    return int('%s%s%s' % (units, hundreds, dozens // 10))


assert integer_14(456) == 645, print(integer_14(456))


def integer_15(num):
    """ 100 <= num < 1000 """
    first_digit = num // 100
    sec_digit = (num % 100) // 10
    third_digit = num % 100 % 10
    return int('%s%s%s' % (sec_digit, first_digit, third_digit))


assert integer_15(123) == 213


def integer_16(num):
    """ 100 <= num < 1000 """
    first_digit = num // 100
    sec_digit = (num % 100) // 10
    third_digit = num % 100 % 10
    return int('%s%s%s' % (first_digit, third_digit, sec_digit))


assert integer_16(123) == 132


def integer_17(num):
    """ num > 999 """
    return num % 1000 / 100


assert integer_17(1300) == 3
assert integer_17(20200) == 2


def integer_18(num):
    """ num > 999 """
    pass


def integer_19(sec):
    ONE_MIN = 60
    return sec // ONE_MIN


assert integer_19(3600) == 60
assert integer_19(3605) == 60


def integer_20(num):
    ONE_MIN, ONE_HOUR = 60, 60
    return num // ONE_MIN // ONE_HOUR


assert integer_20(3625) == 1


def integer_21(seconds):
    """ seconds since last minute """
    ONE_MIN = 60
    return seconds % ONE_MIN


assert integer_21(61) == 1
assert integer_21(125) == 5


def integer_22(seconds):
    """ seconds since last hour """
    return seconds % 3600


def integer_23(seconds):
    """ minutes since last hour """
    ONE_MIN = 60
    return seconds // ONE_MIN


def integer_24(day):
    """
    1 < da < 365
    1st January - Monday
    :return: day of the week
    """
    week = 7
    day_of_week = day % week
    return {0: 'Sun', 1: 'Mon', 2: 'Tue', 3: 'Wed', 4: 'Thurs', 5: 'Fri', 6: 'Sat'}[day_of_week]


assert integer_24(1) == 'Mon'
assert integer_24(18) == 'Thurs'


def integer_25(day):
    """
    1 < day < 365
    1st January - Thurs
    :param day:
    :return:
    """
    week = 7
    day_of_week = (day % week) + 3
    return {0: 'Sun', 1: 'Mon', 2: 'Tue', 3: 'Wed', 4: 'Thurs', 5: 'Fri', 6: 'Sat'}[day_of_week]


assert integer_25(1) == 'Thurs'
assert integer_25(3) == 'Sat'
assert integer_25(7) == 'Wed'


def integer_26(day):
    """
        1 < day < 365
        1st January - Tue
        :param day:
        :return:
        """
    week = 7
    day_of_week = (day % week) + 1
    return {0: 'Sun', 1: 'Mon', 2: 'Tue', 3: 'Wed', 4: 'Thurs', 5: 'Fri', 6: 'Sat'}[day_of_week]


assert integer_26(1) == 'Tue'
assert integer_26(14) == 'Mon'


def integer_27(day):
    """
    1 < day < 365
    1st January - Sun
    :param day:
    :return:
    """
    week = 7
    day_of_week = (day % week) - 1
    return {0: 'Sun', 1: 'Mon', 2: 'Tue', 3: 'Wed', 4: 'Thurs', 5: 'Fri', 6: 'Sat'}[day_of_week]


assert integer_27(1) == 'Sun'
assert integer_27(10) == 'Tue'
assert integer_27(12) == 'Thurs'


def integer_28(days, dw):
    """
     1 < day < 365
     1 < dw < 7
    :param day:
    :return:
    """
    full_week_days = days % 7
    week_day = full_week_days + dw - 1
    return {1: 'Mon', 2: 'Tue', 3: 'Wed', 4: 'Thurs', 5: 'Fri', 6: 'Sun', 7: 'Sat'}[week_day]


assert integer_28(1, 2) == 'Tue'
assert integer_28(11, 2) == 'Fri', integer_28(11, 2)
assert integer_28(1, 1) == 'Mon'


def integer_29(a, b, c):
    total_s = a*b
    cub_s = c**2
    return total_s // cub_s, total_s % cub_s


def integer_30(year):
    pass
