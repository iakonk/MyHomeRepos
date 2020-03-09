def sort_logs(logs_list):
    def func(log):
        _id, rest = log.split(" ", 1)
        return (0, rest, _id) if rest[0].isalpha() else (1,)

    return sorted(logs_list, key=func)


assert sort_logs(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]) == \
       ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]
