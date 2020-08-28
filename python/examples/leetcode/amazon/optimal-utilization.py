"""
https://leetcode.com/discuss/interview-question/373202

Given 2 lists a and b. Each element is a pair of integers where the first integer
represents the unique id and the second integer represents a value. Your task is
to find an element from a and an element form b such that the sum of their values is less or equal
to target and as close to target as possible. Return a list of ids of selected elements.
If no pair is possible, return an empty list.

Example 1:

Input:
a = [[1, 2], [2, 4], [3, 6]]
b = [[1, 2]]
target = 7

Output: [[2, 1]]

Explanation:
There are only three combinations [1, 1], [2, 1], and [3, 1], which have a total sum of 4, 6 and 8, respectively.
Since 6 is the largest sum that does not exceed 7, [2, 1] is the optimal pair.
Example 2:

Input:
a = [[1, 3], [2, 5], [3, 7], [4, 10]]
b = [[1, 2], [2, 3], [3, 4], [4, 5]]
target = 10

Output: [[2, 4], [3, 2]]

Explanation:
There are two pairs possible. Element with id = 2 from the list `a` has a value 5, and element with id = 4
from the list `b` also has a value 5.
Combined, they add up to 10. Similarily, element with id = 3 from `a` has a value 7, and element with id = 2 from `b`
has a value 3.
These also add up to 10. Therefore, the optimal pairs are [2, 4] and [3, 2].
"""


class Solution(object):
    def closest_sum(self, a, b, target):
        if not a or not b:
            return []

        a = sorted(a, key=lambda x: x[1])
        b = sorted(b, key=lambda x: x[1])
        min_diff = float('inf')
        left, right = 0, len(b) - 1
        ans = []
        while left < len(a) and right >= 0:
            id1, val1 = a[left]
            id2, val2 = b[right]
            sum_ = val1 + val2
            curr_diff = target - sum_
            if target - sum_ == min_diff:
                # we found one more sum closest to the target
                ans.append([id1, id2])
            elif sum_ <= target and curr_diff < min_diff:
                # we found new sum closest to the target, better than all previous results
                ans.clear()
                ans.append([id1, id2])
                min_diff = curr_diff
            left += sum_ < target
            right -= sum_ >= target
        return ans


a = [[1, 2], [2, 4], [3, 6]]
b = [[1, 2]]
target = 7
assert Solution().closest_sum(a, b, target) == [[2, 1]]

a = [[1, 3], [2, 5], [3, 7], [4, 10]]
b = [[1, 2], [2, 3], [3, 4], [4, 5]]   
target = 10
ans = Solution().closest_sum(a, b, target)
assert ans == [[2, 4], [3, 2]], ans
