# Write a function to sort the objects in-place on their creation
# sequence number in O(n)O(n) and without any extra space.
# Input: [3, 1, 5, 4, 2]
# Output: [1, 2, 3, 4, 5]


def cyclic_sort(arr):
    i = 0
    while i < len(arr):
        ind = arr[i] - 1
        if arr[i] != arr[ind]:
            arr[i], arr[ind] = arr[ind], arr[i]  # swap
        else:
            i += 1
    return arr


print(cyclic_sort([3, 1, 5, 4, 2]))
