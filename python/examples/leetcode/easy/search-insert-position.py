"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        closest_num, closest_num_ind = float('inf'), float('inf')
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target:
                if nums[mid] - target < closest_num:
                    closest_num = nums[mid] - target
                    closest_num_ind = mid
                hi = mid
            elif nums[mid] < target:
                if target - nums[mid] < closest_num:
                    closest_num = target - nums[mid]
                    closest_num_ind = mid
                lo = mid + 1
            else:
                return mid
        if closest_num_ind < len(nums) - 1:
            closest_num_ind += target > nums[closest_num_ind]
            return closest_num_ind
        elif closest_num_ind == len(nums) - 1:
            closest_num_ind += target > nums[closest_num_ind]
            return closest_num_ind


ans = Solution().searchInsert([1, 3, 5, 6], 5)
assert ans == 2

ans = Solution().searchInsert([1, 3, 5, 6], 2)
assert ans == 1

ans = Solution().searchInsert([1, 3, 5], 4)
assert ans == 2, ans

ans = Solution().searchInsert([1, 3, 5, 6], 7)
assert ans == 4, ans

ans = Solution().searchInsert([1], 0)
assert ans == 0, ans

ans = Solution().searchInsert([1, 2], 0)
assert ans == 0, ans