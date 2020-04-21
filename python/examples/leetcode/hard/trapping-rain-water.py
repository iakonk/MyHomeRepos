class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        right = len(height) - 1
        left_max = right_max = area = left = 0

        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max < right_max:
                area += left_max - height[left]
                left += 1
            else:
                area += right_max - height[right]
                right -= 1
            print(left_max, right_max, area)
        print(area)
        return area


ans = Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
assert ans == 6

ans = Solution().trap([2, 0, 2])
assert ans == 2

ans = Solution().trap([4, 2, 3])
assert ans == 1

ans = Solution().trap([1, 0, 2, 0, 1])
assert ans == 2

ans = Solution().trap([3, 0, 0, 2, 0, 4])
assert ans == 10
