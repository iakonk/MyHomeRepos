"""
This question is asked by Amazon. Given a string representing the sequence of moves a robot vacuum makes,
return whether or not it will return to its original position. The string will only contain L, R, U, and D characters,
representing left, right, up, and down respectively.

Ex: Given the following strings...

"LR", return true
"URURD", return false
"RUULLDRD", return true
"""


class Solution(object):
    def judgeCircle(self, moves_str):
        UD = 0
        LR = 0

        for char in moves_str:
            UD += char == "U"
            UD -= char == "D"

            LR += char == "L"
            LR -= char == "R"
        return UD == 0 and LR == 0


assert not Solution().judgeCircle("URURD")
assert Solution().judgeCircle("RUULLDRD")

assert not Solution().judgeCircle("LL")
assert not Solution().judgeCircle("LLDD")
