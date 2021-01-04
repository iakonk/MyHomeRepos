"""
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
"""


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = max_cnt = 0
        for n in nums:
            cnt += n == 1
            max_cnt = max(max_cnt, cnt)
            cnt = cnt if n else 0

        return max_cnt


ans = Solution().findMaxConsecutiveOnes([1, 1, 0, 1,1,1])
assert ans == 3

ans = Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 0, 1, 0, 1])
assert ans == 2
