def find_missing_number(arr):
    n = len(arr) + 1

    x1 = 1
    for i in range(2, n + 1):
        x1 = x1 ^ i

    x2 = arr[0]
    for i in range(1, n - 1):
        x2 = x2 ^ arr[i]

    return x1 ^ x2


assert find_missing_number([1, 5, 2, 6, 4]) == 3


def find_single_number(arr):
    num = 0
    for i in arr:
        num ^= i
    return num


assert find_single_number([1, 3, 3]) == 1


def f(nums):
    # get the XOR of the all the numbers
    n1xn2 = 0
    for num in nums:
        n1xn2 ^= num

    print(n1xn2, 'zzz')
    # get the rightmost bit that is '1'
    rightmost_set_bit = 1
    while (rightmost_set_bit & n1xn2) == 0:
        rightmost_set_bit = rightmost_set_bit << 1
        print(rightmost_set_bit, 'fff')
    num1, num2 = 0, 0

    for num in nums:
        if (num & rightmost_set_bit) != 0:  # the bit is set
            num1 ^= num
        else:  # the bit is not set
            num2 ^= num

    return [num1, num2]


print(f([1, 4, 2, 1, 3, 5, 6, 2, 3, 5]))
