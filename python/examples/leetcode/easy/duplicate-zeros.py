class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        dup_c = 0
        len_ = len(arr) - 1
        for last in range(len(arr)):
            if last > len_ - dup_c:
                break

            if arr[last] == 0:
                if last == len_ - dup_c:
                    arr[len_] = 0
                    len_ -= 1
                dup_c += 1

        last = len_ - dup_c
        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i+dup_c] = 0
                dup_c -= 1
                arr[i+dup_c] =0
            else:
                arr[i+ dup_c] = arr[i]
        return arr


assert Solution().duplicateZeros([1,0,2,3,0,4,5,0]) == [1,0,0,2,3,0,0,4]