"""
https://leetcode.com/problems/check-if-it-is-a-straight-line/
You are given an array coordinates, coordinates[i] = [x, y],
where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]  ([6,7])
Output: false

Explanation:
http://www.cleverstudents.ru/line_and_plane/line_passes_through_2_points.html
a straight line formula: (x - x0) / (x1 - x0) = (y - y0) / (y1 - y0)
"""


def is_line_straight(coordinates):
    (x0, y0), (x1, y1) = coordinates[:2]
    return all((x - x0) * (y1 - y0) == (x1 - x0) * (y - y0) for x, y in coordinates)


assert is_line_straight([[-3, -2], [-1, -2], [2, -2], [-2, -2], [0, -2]])
assert is_line_straight([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]])
assert is_line_straight([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]) == False
