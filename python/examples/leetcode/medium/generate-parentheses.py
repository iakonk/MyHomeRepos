# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# For example, given n = 3, a solution set is:
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]


class Solution:
    def generateParenthesis(self, n):

        def backtrack(curr_str, open_num, closed_num, res=[]):
            if len(curr_str) == n*2:
                res.append(curr_str)

            if open_num < n:
                backtrack(curr_str + "(", open_num + 1, closed_num)

            if closed_num < open_num:
                backtrack(curr_str + ")", open_num, closed_num + 1)

            return res

        return backtrack("", 0, 0)


ans = Solution().generateParenthesis(2)
assert ans == ['(())', '()()']

"""
curr_str = ''
open_num = 0
closed_num = 0
res = []

if open_num < n #(0 < 2): # recursive call
    curr_str = '('
    open_num = 1
    closed_num = 0
    res = []
    
    if open_num < n # (1 < 2): recursive call
            curr_str = '(('
            open_num = 2
            closed_num = 0
            res = []
            
            if open_num < n #(2 < 2):
                #False

if close_num < open_num # (0<1):
    curr = '()'
    open_num = 1
    closed_num = 1
    
"""


