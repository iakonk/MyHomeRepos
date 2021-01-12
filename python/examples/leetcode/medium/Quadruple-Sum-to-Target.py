"""
Input: [4, 1, 2, -1, 1, -3], target=1
Output: [-3, -1, 1, 4], [-3, 1, 1, 2]
Explanation: Both the quadruplets add up to the target.
"""

class Solution(object):
    def findQuadrupleSum(self, arr, target):
        arr.sort()
        quadruplets = []

        def searchPairs(first, second):
            left, right = second+1, len(arr) - 1
            while left < right:
                curr_sum = arr[first] + arr[second] + arr[left] + arr[right]
                if curr_sum == target:
                    quadruplets.append([arr[first], arr[second], arr[left], arr[right]])
                    left += 1
                    right -= 1
                    while left < right and arr[left] == arr[left -1]:
                        left += 1
                    while left < right and arr[right] == arr[right+1]:
                        right -= 1
                left += curr_sum < target
                right -= curr_sum > target

        for i in range(len(arr) - 3):
            if i and arr[i] == arr[i - 1]:
                continue
            for j in range(i+1, len(arr)-2):
                if j > i+1 and arr[j] == arr[j-1]:
                    continue
                searchPairs(i, j)
        return quadruplets


ans = Solution().findQuadrupleSum([4, 1, 2, -1, 1, -3], 1)
assert ans == [[-3, -1, 1, 4], [-3, 1, 1, 2]]

