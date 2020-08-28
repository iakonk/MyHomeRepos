def fizzBuzz(n):
    next_m1, next_m2, next_m3 = 3, 5, 15
    for ind in range(1, n+1):
        if ind == next_m3:
            print('FizzBuzz')
            next_m3 += 15
            next_m1 += 3
            next_m2 += 5
        elif ind == next_m1:
            print('Fizz')
            next_m1 += 3
        elif ind == next_m2:
            print('Buzz')
            next_m2 += 5
        else:
            print(ind)


if __name__ == '__main__':
    n = 65
    fizzBuzz(n)