"""
Problem Statement #
Given an array of numbers sorted in an ascending order, find the ceiling of a given number ‘key’.
The ceiling of the ‘key’ will be the smallest element in the given array greater than or equal to the ‘key’.

Write a function to return the index of the ceiling of the ‘key’. If there isn’t any ceiling return -1.

Example 1:

Input: [4, 6, 10], key = 6
Output: 1
Explanation: The smallest number greater than or equal to '6' is '6' having index '1'.

Input: [1, 3, 8, 10, 15], key = 12
Output: 4
Explanation: The smallest number greater than or equal to '12' is '15' having index '4'.
"""


class Solution(object):
    def findCeilingOfNum(self, arr, key):
        last_num = arr[len(arr) - 1]
        if key > last_num:
            return -1

        start, end = 0, len(arr) - 1
        while start <= end:
            middle = start + (end - start) // 2
            if key > arr[middle]:
                start = middle + 1
            elif key < arr[middle]:
                end = middle - 1
            else:
                return middle
            print(start, end)
        return start


assert Solution().findCeilingOfNum([1, 3, 8, 10, 15], 12) == 4
assert Solution().findCeilingOfNum([4, 6, 10], 6) == 1


# Given an array of numbers sorted in ascending order, find the floor of a given number ‘key’.
# The floor of the ‘key’ will be the biggest element in the given array smaller than or equal to the ‘key’
#
# Write a function to return the index of the floor of the ‘key’. If there isn’t a floor, return -1.
# Input: [1, 3, 8, 10, 15], key = 12
# Output: 3
# Explanation: The biggest number smaller than or equal to '12' is '10' having index '3'.

class Solution(object):
    def findCeilingOfNum(self, arr, key):
        if key < arr[0]:
            return -1

        start, end = 0, len(arr) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if key < arr[mid]:
                end = mid - 1
            elif key > arr[mid]:
                start = mid + 1
            else:
                return mid
        return end


ans = Solution().findCeilingOfNum([1, 3, 8, 10, 15], 12)
assert ans == 3, ans
