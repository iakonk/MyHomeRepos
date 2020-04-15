class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return nums1
        elif m == 0:
            nums1[:] = nums2[:]
            return nums1

        p1, p2, p = m - 1, n - 1, (m + n) - 1
        while p1 >= 0 and p2 >= 0:
            print(nums1, p1,p2,p)
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            print(nums1)
            p -= 1

        if p2 >= 0:
            nums1[:p2 + 1] = nums2[:p2 + 1]
        return nums1


# ans = Solution().merge([1,2,3,0,0,0],3, [2,5,6], 3)
# print(ans)

# ans = Solution().merge([1],1, [], 0)
# print(ans)

# ans = Solution().merge([],0, [1], 1)
# print(ans)

# ans = Solution().merge([0], 0, [1], 1)
# print(ans)

# ans = Solution().merge([2, 0], 1, [1], 1)
# print(ans)


ans = Solution().merge([4, 0, 0, 0, 0, 0], 1, [1, 2, 3, 5, 6], 5)
print(ans)
