
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
    hundreds, dozens, units = num // 100,  num % 100, num % 100 % 10
    return int('%s%s%s' % (units, hundreds, dozens //10))


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


def integer_21(num):
    """ seconds since last minute """
    ONE_MIN = 60
    return num % ONE_MIN


assert integer_21(61) == 1
assert integer_21(125) == 5


def integer_22(seconds):
    """ seconds since last hour """
    ONE_MIN, ONE_HOUR = 60, 60
    minutes = seconds // ONE_MIN
    hours = minutes // ONE_HOUR

    seconds_passed = hours

def integer_23(num):
    """ minutes since last hour"""
    pass
