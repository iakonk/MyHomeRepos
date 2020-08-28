# Given an array nums of n integers and an integer target, find three integers in nums such
# that the sum is closest to target. Return the sum of the three integers.
# You may assume that each input would have exactly one solution.
# Example:
# Given array nums = [-1, 2, 1, -4], and target = 1.
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        closest_t = float('inf')

        for i, num in enumerate(nums):
            if i and nums[i] == nums[i-1]:
                continue

            left, right = i + 1, n - 1
            while left < right:
                sum_ = nums[i] + nums[left] + nums[right]
                curr_diff = abs(target - sum_)
                min_diff = abs(target - closest_t)
                if curr_diff < min_diff:
                    closest_t = sum_
                left += sum_ < target
                right -= sum_ > target
                if sum_ == target:
                    return closest_t
        return closest_t


ans = Solution().threeSumClosest([-1, 2, 1, -4], 1)
assert ans == 2