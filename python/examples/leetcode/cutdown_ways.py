def countdown_ways(num):

    if num == 0:
        return 0
    if num % 2 == 0:
        return 1 + countdown_ways(num / 2)
    else:
        return 1 + countdown_ways(num - 1)


assert countdown_ways(8) == 4