"""
https://leetcode.com/discuss/interview-question/411357/

Given a 2D grid, each cell is either a zombie 1 or a human 0.
Zombies can turn adjacent (up/down/left/right) human beings into zombies every hour.
Find out how many hours does it take to infect all humans?

Example:

Input:
[[0, 1, 1, 0, 1],
 [0, 1, 0, 1, 0],
 [0, 0, 0, 0, 1],
 [0, 1, 0, 0, 0]]

Output: 2

Explanation:
At the end of the 1st hour, the status of the grid:
[[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [0, 1, 0, 1, 1],
 [1, 1, 1, 0, 1]]

At the end of the 2nd hour, the status of the grid:
[[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1]]
"""
import collections


def min_hours(grid):
    if not grid:
        return

    def neighbours(r, c):
        for nr, nc in ((r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)):
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                yield nr, nc

    def turn_to_zombie():
        """ turn neighbours and create a queue of new zombies """
        new_q = []
        for r, c in queue:
            for nr, nc in neighbours(r, c):
                if not grid[nr][nc]:
                    grid[nr][nc] = 1
                    new_q.append((nr, nc))
        return new_q

    time = 0
    queue = [(i, j) for i, row in enumerate(grid) for j, val in enumerate(row) if val]
    while True:
        queue = turn_to_zombie()
        if not queue:
            break
        time += 1

    return time


grid = [[0, 1, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0]]
assert min_hours(grid) == 2
