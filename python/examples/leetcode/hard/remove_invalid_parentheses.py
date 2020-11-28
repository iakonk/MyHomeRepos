# class Solution(object):
#     def removeInvalidParentheses(self, s):
#         """
#         :type s: str
#         :rtype: List[str]
#         """
#         stack = []
#
#         seen = {}
#         closing, opening = ")", "("
#         for ind, p in enumerate(s):
#             if p == opening:
#                 stack.append(p)
#             elif p == closing:
#                 if stack[-1] != opening:



