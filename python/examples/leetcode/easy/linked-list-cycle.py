# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #         seen = {}
        #         max_cm = len(nums)//2
        #         for num in nums:
        #             seen.setdefault(num, 0)
        #             seen[num] += 1

        #             if seen[num] > max_cm:
        #                 return num
        # import collections
        # aggr = collections.Counter(nums)
        # return max(aggr.keys(), key=aggr.get)
        nums.sort()
        return nums[len(nums) // 2]