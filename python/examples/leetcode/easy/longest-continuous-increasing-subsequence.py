class Solution(object):
    def findLengthOfLCIS(self, nums):
        max_len = pos = 0
        for i in range(len(nums)):
            if i and nums[i-1] >= nums[i]:
                pos = i
            max_len = max(max_len, i - pos + 1)
        return max_len


ans = Solution().findLengthOfLCIS([1,3,5,4,7])
print(ans)

ans = Solution().findLengthOfLCIS([2, 2, 2, 2, 2])
print(ans)
