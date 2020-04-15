# for c in s:
#     open_p = map.get(c)
#     if open_p:
#         prev_p = stack.pop() if stack else None
#         if prev_p != open_p:
#             return False
#     else:
#         stack.append(c)
# return len(stack) == 0


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def is_valid(s, stack):
            if len(s) == 0:
                return True if len(stack) == 0 else False
            else:
                closing_p = map.get(s[0])
                if closing_p:
                    prev = stack.pop() if stack else None
                    return prev == closing_p and is_valid(s[1:], stack)
                else:
                    stack.append(s[0])
                    return is_valid(s[1:], stack)

        map = {")": "(", "}": "{", "]": "["}
        return is_valid(s, [])


ans = Solution().isValid("()")
assert ans

ans = Solution().isValid("()[]{}")
assert ans

ans = Solution().isValid("(]")
assert ans == False

ans = Solution().isValid("([)]")
assert ans == False

ans = Solution().isValid("{[]}")
assert ans

ans = Solution().isValid("[")
assert ans == False
