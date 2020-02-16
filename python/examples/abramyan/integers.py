
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