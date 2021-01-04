"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up
 to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1
 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.

"""


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for idx,  n1 in enumerate(numbers, 1):

            if n1 > target:
                break

            start, end = idx, len(numbers)

            while start < end:
                mid = start + (end-start)//2
                if numbers[mid] + n1 > target:
                    end = mid
                elif numbers[mid] + n1 < target:
                    start = mid + 1
                else:
                    return [idx, mid + 1]


ans = Solution().twoSum([2,7,11,15], 9)
assert ans == [1, 2]

ans = Solution().twoSum([2, 3, 4], 6)
assert ans ==[1,3]


