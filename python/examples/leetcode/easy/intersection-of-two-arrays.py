"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
"""


class Solution(object):
    def find_intersection(self, nums1, nums2):

        def bin_search(pt, arr):
            arr = sorted(arr)
            lo, hi = 0, len(arr)
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if arr[mid] > pt:
                    hi = mid
                elif arr[mid] < pt:
                    lo = mid + 1
                else:
                    return True
            return False

        s1, s2 = set(nums1), set(nums2)
        if len(nums1) < len(nums2):
            return [n for n in s1 if bin_search(n, s2)]
        else:
            return [n for n in s2 if bin_search(n, s1)]


ans = Solution().find_intersection([4, 9, 5], [9, 4, 9, 8, 4])
assert ans == [9, 4]

ans = Solution().find_intersection([1, 2, 2, 1], [2, 2])
assert ans == [2]
