# [0 1 0
#  0 1 0
#  0 1 0
# ]
import collections


def is_hit(x, y):
    return (x, y) in ((2, 1), (2, 2), (2, 3))


def find_first_hit(n, m):
    first_hit = None
    for x in range(0, m):
        for y in range(0, n):
            if is_hit(x, y):
                first_hit = (x, y)
                break
        else:
            continue
    return first_hit


def neighbors(r, c,m,n):
    for nr, nc in ((r + 1, c), (r, c + 1)):
        if 0 <= nr < m and 0 <= nc < n:
            yield nr,nc


def find_ship(n, m):
    ans = [find_first_hit(n, m)]
    queue = collections.deque(ans)
    while queue:
        r, c = queue.pop()
        for nr, nc in neighbors(r, c, m,n):
            if not is_hit(nr, nc):
                continue
            ans.append((nr, nc))
            queue.append((nr, nc))
    return ans


assert find_ship(5, 4) == [(2, 1), (2, 2), (2, 3)], find_ship(5, 4)

