class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        last_ind_map = {c: i for i, c in enumerate(s)}
        stack = []
        seen = set()

        # curr char should be "smaller" the last in a stack
        # curr char ind should be smaller the ind of the prev char in stack
        for i, char in enumerate(s):
            if char not in seen:
                while stack and char < stack[-1] and i < last_ind_map[stack[-1]]:
                    seen.discard(stack.pop())
                seen.add(char)
                stack.append(char)
        return ''.join(stack)


ans = Solution().removeDuplicateLetters("bcabc")
assert ans == "abc"