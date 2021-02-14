class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        arr2.sort()

        def is_distance_found(i):
            """ abs(i - num) <= d"""
            lo, hi = 0, len(arr2) - 1
            while lo <= hi:
                mid = (hi + lo) // 2
                if abs(i - arr2[mid]) <= d:
                    return False
                elif arr2[mid] > i:
                    hi = mid - 1
                else:
                    lo = mid + 1
            return True

        return sum(is_distance_found(i) for i in arr1)


ans = Solution().findTheDistanceValue([4, 5, 8], [10, 9, 1, 8], d=2)
assert ans == 2

ans = Solution().findTheDistanceValue([1, 4, 2, 3], [-4, -3, 6, 10, 20, 30], d=3)
assert ans == 2, ans


class Solution(object):
    def findDistance(self, arr1, arr2, d):
        res = 0
        arr2.sort()  # sort second array

        for num in arr1:  # for every num in arr1
            lo, hi = 0, len(arr2) - 1
            while lo <= hi:  # binary search for num in range in arr2
                middle = (lo + hi) // 2

                if abs(num - arr2[middle]) <= d:
                    break

                if num > arr2[middle]:
                    lo = middle + 1
                else:
                    hi = middle - 1
            else:
                res += 1
        return res


ans = Solution().findDistance([1, 4, 2, 3], [-4, -3, 6, 10, 20, 30], d=3)
print(ans)

# Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
# Output: 2
# Explanation:
# For arr1[0]=4 we have:
# |4-1|=3 > d=2
# |4-8|=4 > d=2
# |4-9|=5 > d=2
# |4-10|=6 > d=2
#
# For arr1[1]=5 we have:
# |5-1|=4 > d=2
# |5-8|=3 > d=2
# |5-9|=4 > d=2
# |5-10|=5 > d=2
#
# For arr1[2]=8 we have:
# |8-1|=7 > d=2
# |8-8|=0 <= d=2
# |8-9|=1 <= d=2
# |8-10|=2 <= d=2
