"""
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2]
Explanation: Your function should return length = 2, with the first two elements of nums being 2.
It doesn't matter what you leave beyond the returned length.
For example if you return 2 with nums = [2,2,3,3] or nums = [2,2,0,0], your answer will be accepted.
"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        slow = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[slow] = nums[i]
                slow += 1
        return slow