import collections

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = collections.defaultdict(list)
        for w in strs:
            sorted_w = ''.join(sorted(w))
            res[sorted_w].append(w)

        return [v for v in res.values()]


ans = Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
assert ans == [["ate","eat","tea"],["nat","tan"],["bat"]]