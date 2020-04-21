class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def find_peak(lo, hi):
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < nums[mid + 1]:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        def find_target(lo, hi):
            while lo <= hi:
                mid = (lo + hi) // 2
                if target < nums[mid]:
                    hi = mid - 1
                elif target > nums[mid]:
                    lo = mid + 1
                else:
                    return mid
            return -1

        n = len(nums)
        # if n == 0:
        #     return -1
        # elif n == 1:
        #     return 0 if target == nums[0] else - 1

        peak_ind = find_peak(0, n - 1)

        # print(rotate_ind)
        # if target == nums[rotate_ind]:
        #     return rotate_ind
        #
        # if rotate_ind == 0:
        #     return find_target(0, n - 1)
        # elif target < nums[0]:
        #     return find_target(rotate_ind + 1, n - 1)
        # else:
        #     return find_target(0, rotate_ind)

# ans = Solution().search([4,5,6,7,0,1,2], 4)
# assert ans==0
#
# ans = Solution().search([4,5,6,7,0,1,2], 0)
# assert ans==4

ans = Solution().search([3, 1], 1)
assert ans==1