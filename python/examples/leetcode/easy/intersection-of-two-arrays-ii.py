"""
Given two arrays, write a function to compute their intersection.

"""


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        nums2.sort()

        def bin_search(target, start, end, arr):
            while start < end:
                mid = (start + end) // 2
                if arr[mid] >= target:
                    end = mid
                else:
                    start = mid + 1

            if 0 <= start < len(arr) and arr[start] == target:
                return start
            else:
                return -1

        ans = []
        start, end = 0, len(nums2)
        for idx, n in enumerate(nums1):
            i = bin_search(n, start, end, nums2)
            if i != -1:
                start = i+1
                ans.append(n)
        print(ans)
        return ans

ans = Solution().intersect([2, 1], [1,2])


# ans = Solution().intersect([1,2,2,1], [2,2])
# assert ans == [2, 2], ans
#
# ans = Solution().intersect([4,9,5], [9,4,9,8,4])
# assert ans == [4,9], ans