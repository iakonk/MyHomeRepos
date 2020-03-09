class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        alphabet = {char: ind for ind, char in enumerate(order)}

        for ind in range(1, len(words)):
            word1 = words[ind - 1]
            word2 = words[ind]

            for w1_char, w2_char in zip(word1, word2):
                if w1_char != w2_char:
                    if alphabet[w1_char] > alphabet[w2_char]:
                        return False
                    break
            else:
                if len(word1) > len(word2):
                    return False
        return True


print(Solution().isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))