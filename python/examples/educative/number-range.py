"""
Problem Statement #
Given an array of numbers sorted in ascending order, find the range of a given number ‘key’.
The range of the ‘key’ will be the first and last position of the ‘key’ in the array.

Write a function to return the range of the ‘key’. If the ‘key’ is not present return [-1, -1].
"""


class Solution(object):
    def findNumRange(self, arr, num):
        def binary_search(find_max_key):
            key_index = -1
            start, end = 0, len(arr)
            while start <= end:
                mid = start + (end - start) // 2
                if num > arr[mid]:
                    start = mid + 1
                elif num < arr[mid]:
                    end = mid - 1
                else:
                    key_index = mid
                    if find_max_key:
                        start = mid + 1
                    else:
                        end = mid - 1
            return key_index

        ans = [-1, -1]
        ans[0] = binary_search(False)
        if ans[0] != -1:
            ans[1] = binary_search(True)
        return ans


assert Solution().findNumRange([4, 6, 6, 6, 9], 6) == [1, 3]
