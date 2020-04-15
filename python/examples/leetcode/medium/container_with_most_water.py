class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        left_i = 0
        right_i = len(height) - 1

        while left_i < right_i:
            min_side = min(height[left_i], height[right_i])
            max_area = max(max_area, min_side * (right_i - left_i))

            if height[left_i] < height[right_i]:
                left_i += 1
            else:
                right_i -= 1
        return max_area


ans = Solution().maxArea([2,3,4,5,18,17,6])
assert ans == 17