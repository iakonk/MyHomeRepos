# heap[k] <= heap[2*k+1] and heap[k] <= heap[2*k+2] for all k
import heapq
import collections


def find_k_largest_numbers(nums, k):
    heap = []
    for i in range(k):
        heapq.heappush(heap, nums[i])
    for i in range(k, len(nums)):
        if nums[i] > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, nums[i])
    return heap


assert find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3) == [5, 12, 11]


# Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.
# [1, 3, 5, 12, 11, 12, 11], K = 2
def find_k_frequent_numbers(nums, k):
    h = []
    aggr = collections.Counter(nums)

    for num, cnt in aggr.items():
        heapq.heappush(h, (cnt, num))
        if len(h) > k:
            heapq.heappop(h)

    return [heapq.heappop(h)[1] for i in range(len(h))]


assert find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2) == [11, 12]


# Given a string, sort it based on the decreasing frequency of its characters.
def sort_character_by_frequency(str):
    aggr = collections.Counter(str)
    h = []
    for char, cnt in aggr.items():
        heapq.heappush(h, (cnt, char))

    string = []
    while h:
        cnt, char = heapq.heappop(h)
        string.extend([char for _ in range(cnt)])

    return ''.join(string)


assert sort_character_by_frequency('abbba') == 'aabbb'


# Design a class to efficiently find the Kth largest element in a stream of numbers.
class KthLargestNumberInStream:
    def __init__(self, nums, k):
        self.k = k
        self.h = []
        for n in nums:
            heapq.heappus(self.h, -n)

    def add(self, num):
        heapq.heappush(self.h, -num)
        return -1
