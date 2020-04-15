class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        for num in nums:
            new_ind = abs(num) - 1
            if nums[new_ind] > 0:
                nums[new_ind] *= -1

        return [ind + 1 for ind in range(len(nums)) if nums[ind] > 0]


ans = Solution().findDisappearedNumbers([1, 1, 2, 4])
print(ans)

ans = Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])
print(ans)
