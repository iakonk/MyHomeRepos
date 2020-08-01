"""
https://leetcode.com/discuss/interview-question/538068/
"""


class Solution(object):
    def battleship(self, n, s, t):

        def make_map():
            """
            :return: {'1A': 0, '1B': 0, '2C': 1}
            """
            m = {}
            for id, one_ship_str in enumerate(s.split(',')):
                start, end = one_ship_str.split(' ')
                for i in range(int(start[0]), int(end[0]) + 1):
                    key_s, key_e = '{0}{1}'.format(i, start[1]), '{0}{1}'.format(i, end[1])
                    m.setdefault(key_s, id)
                    m.setdefault(key_e, id)
            return m

        map = make_map()
        hit_ships = {}
        for one_shot in t.split():
            if one_shot in map:
                id = map[one_shot]
                hit_ships.setdefault(id, 0)
                hit_ships[id] += 1

        hit = sunk = 0
        for id, hit_cells in hit_ships.items():
            s_len = sum(True for k, v in map.items() if v == id)
            sunk += hit_cells == s_len
            hit += 0 < hit_cells < s_len
        return '{0},{1}'.format(sunk, hit)


assert Solution().battleship(3, "1A 1B,2C 2C", "1B") == '0,1'
assert Solution().battleship(4, "1B 2C,2D 4D", "2B 2D 3D 4D 4A") == '1,1'
