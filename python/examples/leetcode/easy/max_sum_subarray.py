# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_win_sum = nums[0]
        win_sum = 0
        for win_end in range(0, len(nums)):
            win_sum += nums[win_end]

            if win_sum > max_win_sum:
                max_win_sum = win_sum

            if win_sum < 0:
                win_sum = 0
        return max_win_sum


Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6