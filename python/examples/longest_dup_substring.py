# Given a string S, consider all duplicated substrings: (contiguous) substrings of S that occur 2 or more times.
# (The occurrences may overlap.)

# Return any duplicated substring that has the longest possible length.
# (If S does not have a duplicated substring, the answer is "".)


def pi(string_):
    result = [0]
    for next_char in string_[1:]:
        prev_char = string_[result[-1]]
        if next_char == prev_char:
            result.append(result[-1] + 1)
        else:
            result.append(0)
    return result


assert pi("arrarra") == [0, 0, 0, 1, 2, 3, 4]
