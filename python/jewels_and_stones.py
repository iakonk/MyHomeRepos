"""
You're given strings J representing the types of stones that are jewels,
and S representing the stones you have.  Each character in S is a type of stone you have.
You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters.
Letters are case sensitive, so "a" is considered a different type of stone from "A"
"""
import time


def timer(func):
    """ """
    def wrapper(*args):
        start_ts = time.time()
        cnt = func(*args)
        print('Finished {} in {} sec, cnt {}'.format(func.__name__, str(time.time() - start_ts), cnt))
    return wrapper


@timer
def find_jewels_slow(jewels, stones):
    """ """
    cnt = 0
    for one_stone in stones:
        for one_jewel in jewels:
           if one_stone == one_jewel:
               cnt +=1
    return cnt


@timer
def find_jewels_faster(jewels, stones):
    """ """
    unique_jewels = set(jewels)
    return len([one_st for one_st in stones if one_st in unique_jewels])


@timer
def numJewelsInStones(J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return sum(s in J for s in S)


@timer
def find_(J, S):
    """ """
    stones = {}
    jewels = {}
    for one_stone in S:
        stones[one_stone] = stones.get(one_stone, 0) + 1

    cnt = 0
    for one_jewel in J:
        if jewels.get(one_jewel):
            continue
        else:
            jewels[one_jewel] = None
            cnt += stones.get(one_jewel, 0)
    return cnt

jewels = "aAAbbbbz"
stones = "az"

find_jewels_slow(jewels, stones)
find_jewels_faster(jewels, stones)
numJewelsInStones(jewels, stones)
find_(jewels, stones)
