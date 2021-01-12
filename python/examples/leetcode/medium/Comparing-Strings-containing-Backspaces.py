"""
Input: str1="xy#z", str2="xzz#"
Output: true
Explanation: After applying backspaces the strings become "xz" and "xz" respectively.
"""


class Solution(object):
    def get_next_valid_index(self, string, index):
        cnt = 0
        while index >= 0:
            if string[index] == '#':
                cnt += 1
            elif cnt > 0:
                cnt -= 1
            else:
                break
            index -= 1
        return index

    def areStringsEqual(self, str1, str2):
        p1, p2 = len(str1) - 1, len(str2) - 1
        while p1 >= 0 or p2 >= 0:
            i1 = self.get_next_valid_index(str1, p1)
            i2 = self.get_next_valid_index(str2, p2)
            if i1 < 0 and i2 < 0:
                return True
            if i1 < 0 or i2 < 0:
                return False
            if str1[p1] != str2[p2]:
                return False
            p1 = i1 - 1
            p2 = i2 - 1
        return True


ans = Solution().areStringsEqual('xy#z', 'xzz#')
assert ans
