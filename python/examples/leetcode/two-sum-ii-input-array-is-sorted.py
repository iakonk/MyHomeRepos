"""
https://leetcode.com/problems/two-sum/submissions/

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
        map_ = {}

        for ind, num in enumerate(numbers):
            diff = target - num
            if diff not in map_:
                map_[num] = ind
            else:
                if map_[diff] != ind:
                    return [ind, map_[diff]]
        return -1



