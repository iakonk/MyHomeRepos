""" https://acmp.ru/index.asp?main=task&id_task=5 """


def get_score():
    """
    :param days_array: 1 <= n <= 31
    :param array_len:  1 ≤ N ≤ 100
    :return:
    """
    even = []  # 4
    odd = []  # 3
    with open('INPUT.TXT', 'r') as rfd:
        array_len, days_array = rfd.readlines()

    if not 1 <= int(array_len) <= 100:
        return
    days_array = days_array.strip().split()
    for i in range(0, int(array_len)):
        day = int(days_array[i])
        if 1 <= day <= 31:
            if day % 2 == 0:
                even.append(str(days_array[i]))
            else:
                odd.append(str(days_array[i]))

    result = "NO"
    if len(even) >= len(odd):
        result = "YES"

    with open('OUTPUT.TXT', 'w') as wfd:
        for el in odd:
            wfd.write(el)
            wfd.write(' ')
        wfd.write('\n')
        for el in even:
            wfd.write(el)
            wfd.write(' ')
        wfd.write('\n')
        wfd.write(result)


get_score()
