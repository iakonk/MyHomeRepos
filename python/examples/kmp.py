# Knuth-Morris-Pratt algorithm
class KMP:

    def pi(self, substring):
        """
        Calculate partial match table: String -> [Int]

        # arrarra -> [0, 0, 0, 1, 2, 3, 4]
        # amar ->    [0, 0, 1, 0]
        # aaoiaa ->  [0, 1, 0, 0, 1, 2]
        """
        res = [0]
        for next_char in substring[1:]:
            prev_char = substring[res[-1]]
            if prev_char == next_char:
                res.append(res[-1] + 1)
            else:
                res.append(0)
        return res

    def search(self, _string, substring):
        mapping = self.pi(substring)
        ret = []
        j = 0
        for i in range(0, len(_string)):
            while j > 0 and _string[i] != substring[j]:
                j = mapping[j - 1]
            if _string[i] == substring[j]:
                j += 1
            if j == len(substring):
                ret.append(i - (j - 1))
                j = mapping[j - 1]

        return ret


res = KMP().pi('arrarra')
assert res == [0, 0, 0, 1, 2, 3, 4]

p2 = "abc"
t2 = "abdabeabfabc"
assert (KMP().search(t2, p2) == [9])
