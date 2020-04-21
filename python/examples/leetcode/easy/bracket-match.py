def bracket_match(text):
    start = 0
    cnt = 0

    for i in range(1, len(text)):
        if text[start:i] == '()':
            continue
        else:
            cnt += 1
    return cnt

    # map = {')': '('}
    # stack = []
    # unmatched_cnt = 0
    #
    # for b in text:
    #     if b in map:
    #         prev_b = stack.pop() if len(stack) > 0 else None
    #         if prev_b != '(':
    #             unmatched_cnt += 1
    #     else:
    #         stack.append(b)
    # unmatched_cnt += len(stack)
    # return unmatched_cnt


ans = bracket_match("(())")
print(ans)