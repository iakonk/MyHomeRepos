def for_1(k, n):
    for i in range(0, k):
        print(n)


def for_2(a, b):
    """ a < b """
    arr = []

    while a != b + 1:
        arr.append(a)
        a += 1
    return arr, len(arr)


assert for_2(-1, 2) == ([-1, 0, 1, 2], 4), for_2(-1, 2)


def for_3(a, b):
    """ a < b """
    arr = []

    exclude = {a, b}
    while b > a:
        if b not in exclude:
            arr.append(b)
        b -= 1
    return arr, len(arr)


assert for_3(-1, 2) == ([1, 0], 2)


def for_4_5_6(price):
    return [price * kg for kg in __range(0.2, 1.1, 0.1)]


def __range(start, end, step=1):
    while start < end:
        yield start
        start += step


def for_7(a, b):
    """ a < b """
    return sum(num for num in __range(a, b + 1))


assert for_7(-1, 2) == 2


def for_8(a, b):
    """ a < b """
    m = 1
    for num in __range(a, b + 1):
        m *= num
    return m


assert for_8(-1, 2) == 0


def for_9(a, b):
    """ a < b """
    m = 0
    for num in __range(a, b + 1):
        m += num ** 2
    return m


def for_10(n):
    """ n > 0 """
    return sum([1 / num for num in __range(1, n + 1)])


def for_11(n):
    pass


def for_15(a, n):
    m = 1
    for _ in __range(a, n + 1):
        m *= a
    return m


def for_16(a, n):
    result = []
    for i in __range(0, n + 1):
        result.append(a ** i)
    return result


assert for_16(3, 5) == [1, 3, 9, 27, 81, 243]


def for_17(a, n):
    """ n> 0"""
    sum_ = 0
    for i in __range(1, n + 1):
        sum_ += a ** i
    return sum_ + 1


assert for_17(2, 3) == 15, for_17(2, 3)


def for_18(a, n):
    sum_ = 0
    for i in __range(1, n + 1):
        if i % 2 == 0:
            sum_ += a ** i
        else:
            sum_ -= a ** i
    return sum_


def for_19(n):
    """ n > 0 """
    m = 1
    for i in __range(1, n + 1):
        m *= i
    return m


def for_20(n):
    def fact(n):
        if n == 0:
            return 1
        return fact(n - 1) * n

    fact_sum = 0
    for i in __range(1, n + 1):
        fact_sum += fact(i)
    return fact_sum


assert for_20(6) == 873


def for_21()
