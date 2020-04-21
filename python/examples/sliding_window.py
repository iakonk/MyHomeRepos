def find_average(k, nums):
    result = []
    start, window_sum = 0, 0

    for ind in range(0, len(nums)):
        window_sum += nums[ind]

        if ind >= k - 1:
            result.append(window_sum / k)
            window_sum -= nums[start]
            start += 1
    return result


assert find_average(5, [1, 3, 2, 6, -1, 4, 1, 8, 2]) == [2.2, 2.8, 2.4, 3.6, 2.8]


def max_sub_array_of_size_k(k, arr):
    max_sum, start = 0, 0

    window_sum = 0
    for ind in range(0, len(arr)):
        window_sum += arr[ind]

        if ind >= k - 1:
            if window_sum > max_sum:
                max_sum = window_sum
            window_sum -= arr[start]
            start += 1
    return max_sum


assert max_sub_array_of_size_k(2, [2, 3, 4, 1, 5]) == 7


def smallest_subarr_with_given_sum(sum_, array):
    window_sum = 0
    window_min_len = array[0]
    window_start = 0

    for ind in range(0, len(array)):
        window_sum += array[ind]

        while window_sum >= sum_:
            window_min_len = min(window_min_len, ind - window_start + 1)
            window_sum -= array[window_start]
            window_start += 1
    return window_min_len


assert smallest_subarr_with_given_sum(7, [2, 1, 5, 2, 3, 2]) == 2
assert smallest_subarr_with_given_sum(7, [2, 1, 5, 2, 8]) == 1
assert smallest_subarr_with_given_sum(8, [3, 4, 1, 1, 6]) == 3


def longest_substring_with_k_dist_chars(string, allowed_dist_chars):
    window_max_size = 0
    window_start = 0
    seen = {}
    for window_end in range(0, len(string)):
        char = string[window_end]
        seen.setdefault(char, 0)
        seen[char] += 1

        while len(seen) > allowed_dist_chars:
            left_most_char = string[window_start]
            seen[left_most_char] -= 1
            if seen[left_most_char] == 0:
                del seen[left_most_char]
            window_start += 1
        window_max_size = max(window_max_size, window_end - window_start + 1)
    return window_max_size


assert longest_substring_with_k_dist_chars("araaci", 2) == 4
assert longest_substring_with_k_dist_chars("araaci", 1) == 2
assert longest_substring_with_k_dist_chars("cbbebi", 3) == 5


def fruits_into_baskets(fruits_list):
    window_start = 0
    max_win_len = 0
    seen = {}

    for ind in range(0, len(fruits_list)):
        one_fruit = fruits_list[ind]
        seen.setdefault(one_fruit, 0)
        seen[one_fruit] += 1

        while len(seen) > 2:
            left_most_fruit = fruits_list[window_start]
            seen[left_most_fruit] -= 1
            if seen[left_most_fruit] == 0:
                del seen[left_most_fruit]
            window_start += 1
        max_win_len = max(max_win_len, ind - window_start + 1)
    return max_win_len


assert fruits_into_baskets(['A', 'B', 'C', 'A', 'C']) == 3
assert fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C']) == 5


def longest_non_repeat_substring(str):
    window_start = 0
    max_window_len = 0
    seen = set()

    for ind in range(0, len(str)):
        char = str[ind]
        if char in seen:
            window_start += 1
        else:
            seen.add(char)
        max_window_len = max(max_window_len, ind - window_start + 1)
    return max_window_len


assert longest_non_repeat_substring("aabccbb") == 3
assert longest_non_repeat_substring("abbbb") == 2
assert longest_non_repeat_substring("abccde") == 5


def get_shortest_unique_substring(arr, str):
    tail, unique_cnt = 0, 0
    seen = {}
    ans = ""
    for head, char in enumerate(str):
        if char not in arr:
            continue
        else:
            if char not in seen:
                unique_cnt += 1
            seen.setdefault(char, 0)
            seen[char] += 1

        while unique_cnt == len(arr):
            if head - tail + 1 == len(arr): # min required len
                return str[tail:head + 1]
            elif not ans or head - tail + 1 < len(ans): # min len found so far
                ans = str[tail: head + 1]

            if str[tail] in seen:
                seen[str[tail]] -= 1
                unique_cnt -= 1
            tail += 1

    # seen = {}
    # min_w_len = float('inf')
    # tail = 0
    # for head, char in enumerate(str):
    #     # if char not in arr and we did`t find so far -> shrink the window & continue
    #     if char not in arr and sum(seen.values()) == 0:
    #         tail += 1
    #         continue
    #     # ["A","B","C","E","K","I"], "KADOBECODEBANCDDDEI"
    #     if char in arr:
    #         seen.setdefault(char, 0)
    #         seen[char] += 1
    #         # # shrink window until duplicate
    #         # while seen[char] > 1:
    #         #     if str[tail] in seen:
    #         #         seen[str[tail]] -= 1
    #         #     tail += 1
    #
    #     # shrink window when it contains all matched characters
    #     if sum(seen.values()) == len(arr):
    #         if min_w_len > head - tail + 1:
    #             min_w_len = head - tail + 1
    #             ans = str[tail: head + 1]
    #         seen = {}
    #         tail = head + 1
    print(ans)
    return ans


ans = get_shortest_unique_substring(["A", "B", "C"], "ADOBECODEBANCDDD")
assert ans == "BANC", ans

ans = get_shortest_unique_substring(["x", "y", "z"], "xyyzyzyx")
assert ans == "zyx"

ans = get_shortest_unique_substring( ["A","B","C","E","K","I"], "KADOBECODEBANCDDDEI")
assert ans == "KADOBECODEBANCDDDEI"
